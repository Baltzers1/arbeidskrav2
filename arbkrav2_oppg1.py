# Utregning av alder
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

while True:                                                                 # bruker while for å kun tillate inputs som er tallverdier
    try:
        print("Hvilket år er du født?")
        A = float(input())  

        print("Din alder vil være", int(2024 - A), "i løpet av 2024" )       # definere verdien til en int for å ikke få med desimal
        break  

    except ValueError: 
        print("Ugyldig input! Vennligst skriv inn et gyldig heltall.")      
        print("")
