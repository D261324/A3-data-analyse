# hier onder staan alle imports 
import csv
import os
from datetime import datetime 

# hier onder staat alles om het csv bestand goed te kunnen gebruiken
menuFile = open("GB.csv", "r", encoding="UTF-8")
outInfoFile = open("outInfo.txt", "w")
reader = csv.DictReader(menuFile, delimiter=";")
data = list(reader)

# hier onder komen alle variable


# !!!!hier onder komt het menu/ hele programma te staan met alle loops en statements!!!!
running = True
while running:    

    print("Welkom bij de contract checker 2020")
    print("1. gemiddelde hoogte van afgegeven vergunningen")
    print("2. top 10 hoogste gebouwen")
    print("3. afgegeven vergunningen na 1-1-2020")
    print("4. afgegeven vergunningen voor buurt X")
    print("w. alle info naar bestand")
    print("x. afsluiten")

    choice = input("\nmaak uw keuze: ")
    
    if choice == "X" or choice == "x":
        exit()

    elif choice == "w":
       outInfoFile.write(f"")

    elif choice == "1":
        print(f"test")

    elif choice == "2":
        print(f"test")

    elif choice == "3":
        print(f"test")

    elif choice == "4":
        print(f"test")

    else:
        print(f"test")

outInfoFile.close
menuFile.close()
