import csv
from datetime import datetime
afterFile = open("GB.csv", "r", encoding="UTF-8")
reader = csv.DictReader(afterFile, delimiter=";")
data = list(reader)

# hier onder staan de variable
datetime_str = '1-1-2020'
datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y')
afterFile = len(data)

# hier onder staan de statements
for license in data:
    if (datetime.strptime(license['Datum_aanvraag'], '%d-%m-%Y') >= datetime_object):
        print(f"{license['Datum_aanvraag']}")
