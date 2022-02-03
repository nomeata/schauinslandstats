#! /usr/bin/env python3

import jsonpickle
import csv

flight_data = jsonpickle.decode(open('flight_data.json', 'r').read())

with open('flight_data.csv', 'w', newline='') as csvfile:
    fieldnames = flight_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for f in flight_data:
        writer.writerow(f)
