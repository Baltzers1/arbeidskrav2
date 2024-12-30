# dictonary 
# author Magnus Baltzersen PY1010-1 24H
# written in VS code

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}


def hent_data(data):                                                                                               # funksjon for å hente data om et land
    land = input("Skriv inn navnet på landet for å hente informasjon: ")                                           # input blir 'land' som under lager vi en if statment slik at om noen taster inn noe som ikke 
    if land in data:                                                                                               # er land som finnes i dictionary-et vårt
        hovedstad, innbyggere = data[land]                                                                         # leser data fra dictionary-et og pakke ut informasjonen for videre bruk i programmet. 
        print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")       # marker starten på en f-streng, slik at vi kan bruke variabler og uttrykk direkte i en streng.
    else:
        print(f"Beklager, jeg har ingen informasjon om {land}.")                                                   # else for if statmenten 


def legg_til_data(data):                                                                                                # funksjon for å legge til et nytt land
    land = input("Skriv inn navnet på landet du vil legge til: ")                                                        
    if land in data:                                                                                                    
        print(f"{land} finnes allerede i databasen.")                                                                   # if statment om landet allerede finnes i dictionary-et
    else:
        hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
        try:                                                                                                            # try statment for et ugyldig verbal for innbyggere
            innbyggere = float(input(f"Skriv inn antall innbyggere i hovedstaden {hovedstad} (i mill.): "))
            data[land] = [hovedstad, innbyggere]
            print(f"{land} er nå lagt til i databasen med hovedstaden {hovedstad} og {innbyggere} mill. innbyggere.")
        except ValueError:
            print("Ugyldig input for innbyggertall. Vennligst skriv et tall.")

def les_opp(data):                                                                          # funksjon for å se hvilke land som ser tilgjengelg i dictionary-et
    print("\n".join(data.keys()))                                                           # data.keys() henter alle nøklene i dictionary-et som en listeaktig struktur
                                                                                            # \n brukes slik at det skal være linjeskift i terminalen om man taster 

def hovedmeny():
    
    valg_til_funksjon = {                                                  # Definer et dictionary som kobler valg til funksjonene ovenfor  
        "1": hent_data,
        "2": legg_til_data,
        "3": les_opp,
    }
    
    while True:                                                            # while loop som gjør at menyen går igjen om den ikke får gyldig valg          
        print("\nHva ønsker du å gjøre?")
        print("1: Hente informasjon om et land")
        print("2: Legge til et nytt land")
        print("3: Se hvilke land som er tilgjengelig")
        print("4: Avslutte programmet")
        
        valg = input("Velg et alternativ (1/2/3/4): ")
        
        if valg == "4":  # Avslutte programmet                             # denne if statment printer 'programmet avslutter' og kjører break/stopp på while loopen
            print("Programmet avsluttes.")
            break
        
        funksjon = valg_til_funksjon.get(valg)                             # her spør vi etter valg inputen for å sjekke om valget finnes i dictionary-et
        if funksjon:
            funksjon(data)                                                 # kall den tilsvarende valget i 'hoved' dictionary-et 'data'for å se om det finnes der.
        else:
            print("Ugyldig valg. Vennligst velg 1, 2, 3 eller 4.")         # om if statmenten retunerer med false så vil denne else statmenten printe 'ugyldig valg'
                                                                           # og while loopen vil fortsette


hovedmeny()                                       