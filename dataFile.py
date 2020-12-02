import csv
dataFile = open("GB.csv","r")
reader = csv.DictReader(dataFile, delimiter=";")
data = list(reader)
# hier onder staan de variable
totalHeight = 0.0
licenceCount = 0
numLicence = len(data)
# avargeHeight = totalHeight / licenceCount

for line in data:
    print(f"hoogte van aangevraagde bouwvergunning: {line['nb_hoogte']}")
    licenceCount += 1
    totalHeight += float(line['nb_hoogte'])

print(f"totale hoogte afgegeven licence: {licenceCount}")
print(f"totale hoogte van afgegeven vergunningen: {totalHeight}")

dataFile.close()