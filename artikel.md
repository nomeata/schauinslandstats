# Höher? Weiter? Schneller!

_Eine etwas anderes Flugdatenauswertung._


Es ist Anfang Oktober, die Wolken verhüllen den Schauinsland, und ans Fliegen ist nicht zu denken. Eine gute Gelegenheit die letzte Saison revue passieren zu lassen. Da ich ein Faible für Statistiken und Schaubilder habe, und für die Colibri-Funcup-Statistik sowieso schon einen Import der DHV-XC-Flugdaten haben, setzte ich mich daran, diesen Datenschatz zu heben.

Dazu habe ich alle Flüge vom Schauinsland von Oktober 2020 bis September 2021 vom DHV-XC-Server geladen („gescrapt“, wie man so schön sagt). Das sind 1454 Flüge, und ein paar „offensichtliche“ Statistiken sind schnell erstellt: Alle Flüge zusammen ergibt das eine Airtime von 39 Tagen, und somit im Schnitt 38 Minuten. Das klingt nach mehr als man intuitiv wohl vermutet, angesichts der vielen 15-Minuten-Abgleiter, aber der Durchschnitt wird eben stark von wenigen langen Flügen beeinflusst. Der Median von 20 Minuten (das heißt, die Hälfte der Flüge sind kürzer als 20 Minuten) klingt da schon richtiger.

Natürlich schauen wir uns erstm einmal die übrlichen Rekorde an: Henning Liebeck hat den längsten (5h10 am 25. April, \#1369640) und den höchsten Flug (3097m am 24. April, \#1368298), der weiteste Flug nach Luftlinie ist Winfried Hetz’ Flug nach Konstanz (20. August, \#1428752). Und Volker Jung flog am häufigsten (275 Flüge), am längsten (4 Tage 4h46), an den meisten Tagen (119), war an den meisten Tagen der erste am Berg (65 Tage), der letzte am Berg (71 Tage), der erste und der letzte (38 Tage) oder gleich der einzige überhaupt (15 Tage) – jeweils mit unüberwindbarem Abstand zum nächsten.

Wirklich überraschend war davon jetzt allerdings nichts – wir brauchen dringend andere Kriterien, am besten solche bei denen auch ich eine Chance habe! Wie wäre es denn mit dem kürzesten Flug? Mich hat doch am 13. Juli der Nordeinschlag direkt zur Holzschlägermatte gespült, so dass ich nach 3½ Minuten schon wieder auf dem Boden stand (\#1388476). Aber nein, selbst diese Trophäe schnappt sich Winfried, dem am 20. August wohl das selbe Schicksal ereilte, nur 4 Sekunden schneller (\#1428752).

Ich muss also weiter suchen, wenn ich einen Preis absahnen möchte. Aber ich habe eine Idee: Immer wieder starte ich in ein Fluggebiet voller frühlich kreisender und steigender Piloten, segele da fröhlich durch die Mitte, finde nichts, stehe wenige Minuten später am Landeplatz und sehe dem Treiben nun von unten zu. Schon wieder wieder alle überholt! Vielleicht können wir wenigstens daraus einen Wettbewerb bauen? Am 24. März habe ich so immerhin 16 andere Piloten überholt (\#1355222). Das soll mir erst einmal einer nachmachen… doch auch hier muss ich mich geschlagen geben; Igor Iegupov schaffte es am 31. März sogar, 18 andere Flieger zu überholen (\#1358988:)! Insgesamt hatte Isabelle Noel am häufigsten das zweifelhafte Vergnügen, unter 69 anderen Fliegern durchzufliegen, dicht gefolgt von Volker mit 58 mal.

Und andersrum, welcher Flug wurde am häufigsten überholt? Den Preis holt sich Henning, der am 24. März knapp vier Stunden in der Luft war; in der Zeit starteten und landeten 34 andere (\#1355044). Insgesamt ließ sich Henning 145 mal überholen. Auch hier geht der zweite Platz an Volker, der 95 überholt wurde.

Ich gebe es auf, die Kriterien auf mich zuzuschneiden. Aber einfach nur „Höher, Weiter, Länger“ ist langweilig. Wie ist es denn mit Weiter und Länger, aber ohne hoch? Leider zeigt DHV-XC nicht den kumulierten Höhengewinn an, sonst würde ich jetzt schauen, wer auch ohne Steigen am längsten Fliegen kan. Als nächste Näherung nehme ich eben Flüge ohne Startüberhöhung (maximale Höhe < 1170m). Da hat Stefan Meier mit 2h08 den längsten Flug (8. September, \#1438309) und Martin Bloße den weitesten (10. Juni, über Horben bis hinter Wittnau, \#1386446).

Ähnlich können wir uns die A-Schirm-Piloten anschauen: Hier glänzt Isabelle Noel mit dem weitesten Flug zur Wonnhalde vor (13. März, \#1359537) und Rafael Grüninger flog am 16. Juni gleichzeitig am höchsten und längsten (2h52, 2217m, \#1390830).

Damit habe ich meinen Appetit nach unnötiger Statistik gestillt. Deinen noch nicht? Dann schreib mir doch per Slack was du wissen willst – oder mach es selber! Die Statistiken wurden alle mit wenigen Zeilen schnödem Python-Code erstellt, der in einem Jupyter-Notebook steht. Dieses kannst du von <https://github.com/nomeata/schauinslandstats> herunter laden oder per <https://mybinder.org/v2/gh/nomeata/schauinslandstats/master?urlpath=tree/Schauinsland.ipynb> direkt im Browser öffnen.

PS: Die Nummern sind die Flugnummern auf dem DHV-XC-Server. Wenn ihr in der Adresse <https://www.dhv-xc.de/leonardo/index.php?op=show_flight&flightID=1388476> die Nummer ersetzt kommt ihr direkt zu dem jeweils erwähnten Flug.

_Bildunterschrift zum Schaubild_: Ab 12 gehts hoch! Jeder Kreis ist ein Flug am Schauinsland. Die X-Achse ist der Startzeitpunkt (Sommerzeit _nicht_ korrigiert) und die Y-Achse die Flugdauer. Die Farbe gibt die Schirmkategorisierung an.
