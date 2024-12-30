#
#
#

import math

def utregning(a, b):
    omkrets = b + math.sqrt(a**2 + b**2) + math.pi*a            # Beregner omkretsen i en samlet formel
    areal = ((math.pi * a**2 + a * b)/2)                        # Beregner arealet i en samlet formel
    return omkrets, areal

while True:
    print('\nFor å beregne areal og omkretsen av figuren, vennligst tast inn de verdiene for a og b.')
    print('Hvor a er den siden av trekanten som deler lengde med halvsirkelens diameter')
    print('Hvor a er den siden av trekanten som deler lengde med halvsirkelens diameter')
    
    try:
        a = float(input("Tast inn verdi for a: "))
        b = float(input("Tast inn verdi for b: "))

        omkrets, areal = utregning(a, b)

        print(f"Omkretsen av figuren er: {omkrets:.2f}\nOg arealet av figuren er: {areal:.2f}")

    except ValueError:
        print('Vennligst skriv inn gyldige tall for a og b')
