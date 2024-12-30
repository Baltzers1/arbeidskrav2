# Utregning pizza per elev
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

while True:                                                                 # bruker while loop for at programmet skal fortsette å kjøre om try funksjonen under feiler
    try:                                                                    # try funksjon slik at vi kan ha en feilmelding og et nytt forsøk om inputen under gjøre at 
        antall_elever = int(input('Skriv inn antall elever:' ))             # funksjonen ender i en error
        pizzaer = 0.25 * antall_elever 
       
        def round_up(pizzaer):
            if pizzaer % 1 != 0:                                            # hvis tallet har desimaler
                return int(pizzaer) + 1                                     # legg til 1 for å runde opp
            return int(pizzaer)                                             # hvis det allerede er et heltall


        print("Du må handle inn", round_up(pizzaer), "antall pizzar" )      # definere verdien til en int for å ikke få med desimal
        break                                                               # break stopper while loopen

    except ValueError:                                                      # her har jeg kopiert fra tidligere oppgave. 
        print("Ugyldig input! Vennligst skriv inn et gyldig heltall.")      
        print("")
