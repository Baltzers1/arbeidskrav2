# areal og omkrets av figur
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

import math

def utregning(a, b):                                            # funksjon som gjør utregningen 
    omkrets = b + math.sqrt(a**2 + b**2) + math.pi*a            # beregner omkretsen i en samlet formel som jeg satt sammen for å forenkle koden
    areal = ((math.pi * a**2 + a * b)/2)                        # beregner arealet i en samlet formel
    return omkrets, areal

while True:                                                                                                    # while loop slik at ikke programmet stopper om en ugyldig verdi blir tastet inn
    print('\nFor å beregne areal og omkretsen av figuren, vennligst tast inn de verdiene for a og b.')         # \n for linjeskift
    print('Hvor a er den siden av trekanten som deler lengde med halvsirkelens diameter')
    print('Hvor a er den siden av trekanten som deler lengde med halvsirkelens diameter')
    
    try:                                                                                                       # try funksjon for at man skal funne gjenkjenne inputs som ikke vil være gyldige inn i utregningen
        a = float(input("Tast inn verdi for a: "))
        b = float(input("Tast inn verdi for b: "))

        omkrets, areal = utregning(a, b)                                                                       # her hentes funksjonen utregning med verbalene a og b som ble definert om inputs over

        print(f"Omkretsen av figuren er: {omkrets:.2f}\nOg arealet av figuren er: {areal:.2f}")                # print av svaret med en begrensing på 2 desimaler i float verbalen. \n for linjeskift

    except ValueError:
        print('Vennligst skriv inn gyldige tall for a og b')
