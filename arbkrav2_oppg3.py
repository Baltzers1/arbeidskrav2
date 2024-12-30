# Fra Grader til radianer
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

import numpy as np                                                                                  # importerer numpy for å kunne bruke numpy.pi velger
                                                                                                    # å gi den aliaset np
def grad_til_rad(v_grad):                                                                           # definerer grader til radianer ved å gi formelen som tar inputen
    v_rad = v_grad * np.pi / 180                                                                    # v_grad og returnerer resultatet v_rad        
    return v_rad

while True:                                                      
    try:
        v_grad = float(input('Skriv inn gradtallet:' ))                                             # her spørre det etterv_grad som vi gir som input 
                                                                                                    # den kommer igjen i neste linje
        v_rad = grad_til_rad(v_grad)
        print("Vinkelen", v_grad, "grader tilsvarer" , round(v_rad,4) , "radianer.")                # her blir inputen satt som en verbal i utregningen som ble     
        break                                                                                       # definert i starten av koden, før while loopen.             

    except ValueError: 
        print("Ugyldig input! Vennligst skriv inn et gyldig tall.")      
        print("")

        