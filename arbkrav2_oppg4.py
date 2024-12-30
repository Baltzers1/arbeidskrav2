# arbeidskrav_2 Oppgave_4 v2.0
# author Magnus Baltzersen PY1010-1 24H
# written in VS code

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}


def hent_data(data):                                                                                               # Funksjon for å hente data om et land
    land = input("Skriv inn navnet på landet for å hente informasjon: ")
    if land in data:
        hovedstad, innbyggere = data[land]                                                                         # Denne linjen brukes til å lese data fra dictionary-en 
        print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")       # og pakke ut informasjonen for videre bruk i programmet.
    else:
        print(f"Beklager, jeg har ingen informasjon om {land}.")


def legg_til_data(data):                                                                                                # Funksjon for å legge til et nytt land
    land = input("Skriv inn navnet på landet du vil legge til: ")
    if land in data:
        print(f"{land} finnes allerede i databasen.")
    else:
        hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
        try:
            innbyggere = float(input(f"Skriv inn antall innbyggere i hovedstaden {hovedstad} (i mill.): "))
            data[land] = [hovedstad, innbyggere]
            print(f"{land} er nå lagt til i databasen med hovedstaden {hovedstad} og {innbyggere} mill. innbyggere.")
        except ValueError:
            print("Ugyldig input for innbyggertall. Vennligst skriv et tall.")


# Funksjon for å legge se hvilke land som ser tilgjengelg
def les_opp(data):
    print("\n".join(data.keys()))

def hovedmeny():
    while True:
        print("\nHva ønsker du å gjøre?")                                                   # \n brukes slik at det skal være linjeskift i terminalen om man taster 
        print("1: Hente informasjon om et land")                                            # inn en ugyldig verdi. 
        print("2: Legge til et nytt land")
        print("3: Se hvilke land som er tilgjengelig")
        print("4: Avslutte programmet")
        
        valg = input("Velg et alternativ (1/2/3/4): ")

        if valg == "1":
            hent_data(data)
        elif valg == "2":
            legg_til_data(data)
        elif valg == '3':
            les_opp(data)
        elif valg == "4":
            print("Programmet avsluttes.")
            break
        else:
            print("Ugyldig valg. Vennligst velg 1, 2 eller 3.")

# Start programmet
hovedmeny()