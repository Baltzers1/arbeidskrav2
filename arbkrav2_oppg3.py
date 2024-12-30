# Fra Grader til radianer
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 

import math                                                                                  # importerer math for å bruke math.pi

def grad_til_rad(v_grad):                                                                    # funksjon for utregning ved å gi formelen som tar inputen
    v_rad = v_grad * math.pi / 180                                                           # v_grad og returnerer resultatet v_rad        
    return v_rad                                                                             

while True:                                                                                  # while loop så ikke programmet lukker seg om vi får en error
    try:
        v_grad = float(input('Skriv inn gradtallet:' ))                                      # spør etter v_grad som vi gir som input  den kommer igjen i neste linje
                                                                                                  
        v_rad = grad_til_rad(v_grad)
        print("Vinkelen", v_grad, "grader tilsvarer" , round(v_rad,4) , "radianer.")         # printer tekst + v_grad som allerede er definert som en float og v_rad    
        break                                                                                # med fire desimaler avrundet    

    except ValueError:                                                                       # om try funksjonen feiler så printes dette og while loopen fortsetter
        print("Ugyldig input! Vennligst skriv inn et gyldig tall.")      
        print("")
        