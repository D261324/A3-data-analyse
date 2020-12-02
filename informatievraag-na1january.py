import csv
from datetime import datetime
afterFile = open("GB.csv", "r", encoding="UTF-8")
reader = csv.DictReader(afterFile, delimiter=";")
data = list(reader)

# hier onder staan de variable
datetime_str = '1-1-2020'
datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y')
permitsAfterDate = 0

# hier onder staan de statements
for permit in data:
   if (datetime.strptime(permit['Datum_aanvraag'], '%d-%m-%Y') >= datetime_object):
      permitsAfterDate += 1
   
print(permitsAfterDate)
