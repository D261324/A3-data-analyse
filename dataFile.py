import csv
dataFile = open("GB.csv","r")
reader = csv.DictReader(dataFile, delimiter=";")
data = list(reader)
# hier onder staan de variable
totalHeight = 0.0
totalLicenses = len(data)
averageHeight = 0
# avargeHeight = totalHeight / licenseCount

for line in data:
    totalHeight += float(line['nb_hoogte'])

averageHeight = totalHeight / totalLicenses

print(f"Aantal afgegeven vergunningen: {totalLicenses}")
print(f"Totale hoogte van afgegeven vergunningen: {round(totalHeight, 1)} meter")
print(f"Gemiddelde hoogte van alle gebouwen: {round(averageHeight, 2)} meter")

dataFile.close()