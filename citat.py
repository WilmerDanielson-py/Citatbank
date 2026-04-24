"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""

import random
import json


def ladda_citat_fran_fil(filnamn):
    
    f = open(filnamn, "r", encoding = "utf8")
    citat_dict = json.load(f)
    return citat_dict


def spara_citat_till_fil(citatlista, filnamn):
    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    with open(filnamn, "w", encoding="utf8") as f:
        json.dump(citatlista, f)
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    pass


def visa_alla_citat(citatlista):
    
    for i , d in enumerate(citatlista):
        print(f"{i+1}. {d['person']} - {d['citat']}")

def lagg_till_citat(citatlista):
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i
    
    Returnerar:
        bool: True om citatet lades till, False annars
    """
    nytt_citat = input("Ange Citatet: ")
    författare = input("Ange Författare: ")
    citatlista.append({"citat": nytt_citat, "person": författare})
    if nytt_citat and författare:
        return True
    else:        
        return False
    

    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"
    pass


def slumpa_citat(citatlista):

    if not citatlista:
        print("Inga citat att visa.")
        return
    else:
        random_citat = random.choice(citatlista)
        print(f"{random_citat['person']} - {random_citat['citat']}")


def huvudprogram():
    ladda_citat_fran_fil("data.json")
    
    val = input("Välj ett alternativ:\n1. Spara citat\n2. Visa alla citat\n3. Lägg till citat\n4. Slumpa citat\n5. Avsluta\n---> ")
    citat = ladda_citat_fran_fil("data.json")
    if val == "1":
        spara_citat_till_fil(citat, "data.json")
    elif val == "2":
        visa_alla_citat(citat)
    elif val == "3":
        lagg_till_citat(citat)
        spara_citat_till_fil(citat, "data.json")
        
        
    elif val == "4":
        slumpa_citat(citat)
    elif val == "5":
        print("Avslutar programmet.")
        
    # 2. Skapa en while-loop som visar menyn
        # 3. Hantera användarens val med if/elif/else
        # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
        # 5. Vid val 4: avsluta loopen
        pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()