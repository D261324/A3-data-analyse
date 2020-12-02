import os
import csv

dataFile = open("GB.csv", "r")
reader = csv.DictReader(dataFile, delimiter=';')
data = list(reader)

running = True
while running:
   os.system('cls')

   userNeighborhood = input("Vul een buurt in: ").lower()
   permitsInNeighborhood = 0

   for line in data:
      if line["Wijk"].lower() == userNeighborhood:
         permitsInNeighborhood += 1

   if permitsInNeighborhood == 0:
      permitsInNeighborhood = "geen"
   
   print(f"Er zijn {permitsInNeighborhood} vergunningen afgegeven voor gebouwen in {userNeighborhood.capitalize()}.")

   stop = input("\nDruk op Enter om door te gaan of typ 'X' om te stoppen")
   if stop.lower() == "x":
      running = False