#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 python3Packages.dateutil python3Packages.matplotlib python3Packages.requests python3Packages.requests-cache python3Packages.beautifulsoup4 python3Packages.jsonpickle

import requests
import requests_cache
from bs4 import BeautifulSoup
import datetime
import re
import jsonpickle
import os
from collections import defaultdict

FIRST_DAY = datetime.date(2019,9,16)
LAST_DAY = datetime.date(2022,12,31)


#
# Web scraping section
#

# We want all requests to be cached transparently
# We cache the flight lists for up to 5 mins (see expire_after)
# The actual flight views are always cached. If someone complains that a later
# added comment was not picked up, delete cache.sqlite and re-run the script
requests_cache.install_cache(backend='sqlite')

# First we find out which flights ids might be relevant
# For that we scrape the list_flights view, page for page, until we are done or
# see too old flights
flight_ids = set()

def scrape_page_for_flights(url):
  page_num = 1
  done = False
  while not done:
      with requests_cache.enabled(backend='sqlite', expire_after=300):
          r = requests.get(f"{url}&page_num={page_num}")
          r.encoding = 'utf8'
          soup = BeautifulSoup(r.text, 'html.parser')
          #print (soup.prettify())

          rows = soup.find('table', class_ = 'listTable').find_all('tr')
          # empty result? lets abort
          if len(rows) <= 1:
              print(f"No rows at page {page_num}\n:{r.text}")
              done = True
          for row in rows:
              if row.find_all('td', class_='SortHeader'):
                  continue
              date_str = row.find(name='td', class_='dateString').text.strip()
              date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

              flight_id = row['id'].lstrip("row_")

              if date < FIRST_DAY:
                  done = True # stop loading more pages if we see old flights
              elif date <= LAST_DAY:
                  flight_ids.add(flight_id)
              else:
                  pass

          page_num += 1

# schaui-flüge
scrape_page_for_flights("https://www.dhv-xc.de/leonardo/index.php?op=list_flights&takeoffID=9306&season=0&year=0&month=0&day=0")
# lindenberg-flüge
scrape_page_for_flights("https://www.dhv-xc.de/leonardo/index.php?op=list_flights&takeoffID=11362&season=0&year=0&month=0&day=0")


flight_ids.remove("1335432") # bad flight

print(f"Total number of flights: {len(flight_ids)}")

# Now we go look at each flight id and scrape the show_flight view
flight_data=[]
for flight_id in flight_ids: # list(flight_ids)[:100]: # flight_ids:
    with requests_cache.enabled(backend='sqlite'):
        #print(f"Fetching flight {flight_id}...")
        r = requests.get(f"https://www.dhv-xc.de/leonardo/index.php?op=show_flight&flightID={flight_id}")
        r.encoding = 'utf8'
        soup = BeautifulSoup(r.text, 'html.parser')
        #print (soup.prettify())

        fd = {}
        fd['flightid'] = flight_id

        # Name and date
        pilot_pos = soup.find(id="pilot_pos")
        if not pilot_pos:
            print(soup.prettify())
            print(flight_id)
        pilot_str = soup.find(id="pilot_pos").text
        pilot_re = re.compile(r'\s*Pilot:\s*(.*)Datum:\s*(\d\d/\d\d/\d\d\d\d)\s*')
        m = pilot_re.match(pilot_str)
        fd['name'] = m.group(1).strip()
        fd['date'] = datetime.datetime.strptime(m.group(2), '%d/%m/%Y').date()

        # Pilot id
        pilotid_str = soup.find(id="pilot_pos").a['href']
        pilotid_re = re.compile(r"javascript:pilotTip\.newTip\('.*',.*,.*,.*,.*,\s*'([\d_]+)','.*'\s*\)")
        m = pilotid_re.match(pilotid_str)
        # we strip the 0_ prefix for consistency, e.g. with the EXTRA_PILOTS filter
        fd['pilotid'] = m.group(1).strip().lstrip('0_')

        # Take off and landing
        fd['take_off'] = soup.find(id='takeoffAddPos').text
        fd['landing'] = soup.find(name='td',text='Landeplatz').parent.find_next_sibling(name='tr').td.div.text

        # Flight time
        take_off_time_str = soup.find(name='div',text='Startplatz').parent.find_next_sibling(name='td').div.span.text
        take_off_time_re = re.compile(r'(\d+):(\d+):(\d+)')
        m = take_off_time_re.match(take_off_time_str)
        fd['take_off_time'] = datetime.timedelta(
            hours=int(m.group(1)),
            minutes=int(m.group(2)),
            seconds=int(m.group(3)))

        # Duration
        duration_str = soup.find(name='td',text='Dauer').find_next_sibling(name='td').text
        duration_re = re.compile(r'(\d+):(\d+):(\d+)')
        m = duration_re.match(duration_str)
        fd['duration'] = datetime.timedelta(
            hours=int(m.group(1)),
            minutes=int(m.group(2)),
            seconds=int(m.group(3)))

        # Max altitude
        max_alt_str = soup.find(name='td',text='Grösste Höhe(GPS)').find_next_sibling(name='td').span.text
        alt_re = re.compile(r'(\d+).m')
        m = alt_re.match(max_alt_str)
        fd['max_alt'] = int(m.group(1))

        # Luftlinie
        luftlinie_str = soup.find(name='div',text='Luftlinie').parent.find_next_sibling(name='td').div.text
        luftlinie_re = re.compile(r'(\d+\.\d+)\skm\s\(.*\)')
        m = luftlinie_re.match(luftlinie_str)
        fd['luftlinie'] = float(m.group(1))

        # Schirm
        fd['schirm'] = soup.find(name='img',class_='brands')['title']

        flight_data.append(fd)

open('flight_data.json','w').write(jsonpickle.encode(flight_data))
