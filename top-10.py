import csv

dataFile = open("./GB.csv", "r")
reader = csv.DictReader(dataFile, delimiter=';')
data = list(reader)

data_sorted = sorted(data, key=lambda row: float(row['nb_hoogte']), reverse=True)


print("------------------")
for i in range(10):
   item = data_sorted[i]
   print(f"{item['Adres']} {item['Huisnummer']} is {item['nb_hoogte']} meter hoog")

dataFile.close()

