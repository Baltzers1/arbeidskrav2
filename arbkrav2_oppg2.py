# Utregning pizza per elev
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

while True:                                                                 # bruker while for å kun tillate inputs som er tallverdier
    try:
        antall_elever = int(input('Skriv inn antall elever:' ))
        pizzaer = 0.25 * antall_elever 
       
        def round_up(pizzaer):
            if pizzaer % 1 != 0:                                                     # Hvis tallet har desimaler
                return int(pizzaer) + 1                                              # Legg til 1 for å runde opp
            return int(pizzaer)                                                      # Hvis det allerede er et heltall


        print("Du må handle inn", round_up(pizzaer), "antall pizzar" )       # definere verdien til en int for å ikke få med desimal
        break  

    except ValueError: 
        print("Ugyldig input! Vennligst skriv inn et gyldig heltall.")      
        print("")
