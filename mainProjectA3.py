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
inputPassedCheck = None


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

   if inputPassedCheck == 0:
      print("\nFunctie niet gevonden.")
   
   choice = input("\nMaak uw keuze: ").lower()
   
   inputPassedCheck = 0
    
   if choice == "1" or choice == "w":
      inputPassedCheck = 1
      os.system("cls")
   #  Press 1:
      totalPermits = len(permits)
      totalHeight = 0.0
      

      for permit in permits:
         totalHeight += float(permit['nb_hoogte'])

      averageHeight = totalHeight / totalPermits
      averageHeightString = (f"Gemiddelde hoogte van alle gebouwen: {round(averageHeight, 2)} meter.")

      print(f"Aantal afgegeven vergunningen: {totalPermits}")
      print(f"Totale hoogte van afgegeven vergunningen: {round(totalHeight, 1)} meter")
      print(averageHeightString)
   #  End Press 1

   if choice == "2" or choice == "w":
      inputPassedCheck = 1
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
      inputPassedCheck = 1
      os.system("cls")
   #  Press 3
      datetime_str = '1-1-2020'
      datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y')
      permitsAfterDate = 0

      for permit in permits:
         if (datetime.strptime(permit['Datum_aanvraag'], '%d-%m-%Y') >= datetime_object):
            permitsAfterDate += 1
      
      permitsAfterDateString = (f"Er zijn {permitsAfterDate} vergunningen afgegeven na {datetime_str}.")
      print(permitsAfterDateString)
   #  End Press 3

   if choice == "4" or choice == "w":
      inputPassedCheck = 1
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
      inputPassedCheck = 1
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
      outInfoFile.write(f"----------------------------------------\n")
      print("Gegevens worden naar het bestand geschreven zodra u het programma afsluit (X).")
   
   # if choice == "x":
   #    inputPassedCheck = 1
   #    print("Tot de volgende keer!")
   #    running = False
   #    exit()
   if choice:
      if choice != "x":
         choice = input("\nDruk op enter om door te gaan of typ 'X' om te stoppen: ").lower()
      if choice == "x":
         os.system("cls")
         inputPassedCheck = 1
         print("Tot de volgende keer!")
         running = False
         exit()
         continue


   if inputPassedCheck == 0:
      print("Functie niet gevonden.")
      continue
   # inputPassedCheck = 0


outInfoFile.close()
dataFile.close()
