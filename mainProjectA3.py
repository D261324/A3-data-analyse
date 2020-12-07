# hier onder staan alle imports 
import csv
import os
from datetime import datetime 

# hier onder staat alles om het csv bestand goed te kunnen gebruiken
dataFile = open("GB.csv","r")
reader = csv.DictReader(dataFile, delimiter=";")
permits = list(reader)
outInfoFile = open("outInfo.txt", "w")

# hier onder komen alle variable
averageHeightString = ""
topTen = []
permitsAfterDateString = ""
permitsInNeighborhoodString = ""


# !!!!hier onder komt het menu/ hele programma te staan met alle loops en statements!!!!
running = True
while running:    
   os.system("cls")
   print("1. Gemiddelde hoogte van afgegeven vergunningen")
   print("2. Top 10 hoogste gebouwen")
   print("3. Afgegeven vergunningen na 1-1-2020")
   print("4. Afgegeven vergunningen voor buurt X")
   print("W. Alle info naar bestand")
   print("X. Afsluiten")

   choice = input("\nMaak uw keuze: ").lower()
    
   if choice == "1" or choice == "w":
      os.system("cls")
   #  Press 1:
      totalPermits = len(permits)
      totalHeight = 0.0
      

      for permit in permits:
         totalHeight += float(permit['nb_hoogte'])

      averageHeight = totalHeight / totalPermits
      averageHeightString = (f"Gemiddelde hoogte van alle gebouwen: {round(averageHeight, 2)} meter")

      print(f"Aantal afgegeven vergunningen: {totalPermits}")
      print(f"Totale hoogte van afgegeven vergunningen: {round(totalHeight, 1)} meter")
      print(averageHeightString)
   #  End Press 1

   if choice == "2" or choice == "w":
      topTen = []
      os.system("cls")
   #  Press 2:
      permits_sorted = sorted(permits, key=lambda row: float(row['nb_hoogte']), reverse=True)

      for i in range(1, 11):
         item = permits_sorted[i]
         topTen.append(f"{i} | {item['Adres']} {item['Huisnummer']} is {item['nb_hoogte']} meter hoog")
         print(f"{topTen[i-1]}")
      
      # print("\n")
   #  End Press 2

   if choice == "3" or choice == "w":
      os.system("cls")
   #  Press 3
      datetime_str = '1-1-2020'
      datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y')
      permitsAfterDate = 0

      for permit in permits:
         if (datetime.strptime(permit['Datum_aanvraag'], '%d-%m-%Y') >= datetime_object):
            permitsAfterDate += 1
      
      permitsAfterDateString = (f"Er zijn {permitsAfterDate} vergunningen afgegeven na {datetime_str}")
      print(permitsAfterDateString)
   #  End Press 3

   if choice == "4" or choice == "w":
      os.system('cls')
   #  Press 4
      userNeighborhood = input("Vul een buurt in: ").lower()
      permitsInNeighborhood = 0

      for permit in permits:
         if permit["Wijk"].lower() == userNeighborhood:
            permitsInNeighborhood += 1

      if permitsInNeighborhood == 0:
         permitsInNeighborhood = "geen"

      os.system("cls")
      permitsInNeighborhoodString = (f"Er zijn {permitsInNeighborhood} vergunningen afgegeven voor gebouwen in {userNeighborhood.capitalize()}.")
      print(permitsInNeighborhoodString)
      #  End Press 4

   if choice == "w":
      now = datetime.now()
      now = now.strftime("%d-%m-%Y %H:%M:%S")
      os.system("cls")
      outInfoFile.write(f"Data gegenereerd op {now}:\n")
      outInfoFile.write(f"1. {averageHeightString}\n")
      outInfoFile.write(f"2. Hoogste gebouwen:\n")

      for item in topTen:
         outInfoFile.write(f"\t{item}\n")

      outInfoFile.write(f"3. {permitsAfterDateString}\n")
      outInfoFile.write(f"4. {permitsInNeighborhoodString}\n")
      print("Typ 'X' om te stoppen en de informatie naar het bestand te schrijven.")
   
   if choice == "x":
      exit()

   stop = input("\nDruk op enter om door te gaan of typ 'X' om te stoppen")
   if(stop == "X" or stop == "x"):
      running = False

outInfoFile.close
dataFile.close()
