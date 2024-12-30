# Utregning av alder
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

while True:                                                                 # bruker while loot for at programmet ikke skal stoppe om det er en ugyldig verdi som input
    try:                                                                    # try funksjon for å sjekke om input vil fungere i koden
        print("Hvilket år er du født?")
        A = float(input())  

        print("Din alder vil være", int(2024 - A), "i løpet av 2024" )       # definere verdien til en int for å ikke få med desimal
        break                                                                # brak stopper while loopen for programmet er ferdig når linjen over har blitt lest 

    except ValueError:                                                       # except som brukes om try funksjonen retunerer false 
        print("Ugyldig input! Vennligst skriv inn et gyldig heltall.")      
        print("")                                                            # dette er for jeg ønsker et mellomrom mellom teksten over og neste tekst om inputen er ugyldig
