# Plotting av funksjon
# Forfatter: Magnus Baltzersen 22.10.24 
# Skrevet i VS code 


import numpy as np
import matplotlib.pyplot as plt

# Definer x-verdier og funksjonen f(x)
x = np.linspace(-10, 10, 200)                                      # Genererer 200 punkter fra -10 til 10 som vist i oppgaveteksen
funk_x = -x**2 - 5                                                 # Funksjonen f(x)

# Plot funksjonen
plt.plot(x, funk_x, label=r'$f(x) = -x^2 - 5$', color='blue')      # plt.plot(x, f_x): Tegner grafen basert på x-verdiene og tilhørende 𝑓(𝑥)f(x)-verdierlabel: Gir grafen 
                                                                   # et navn som kan vises i en legende. Her bruker vi LaTeX-syntaks (r'$f(x) = -x^2 - 5$') for å få fin matematisk formatering.

plt.title("Grafen til f(x) = -x^2 - 5")                            # Legger til en tittel på grafen. 
plt.xlabel("x")                                                    # Navngir x aksen
plt.ylabel("f(x)")                                                 # Navngir y aksen
plt.axhline(0, color='black', linewidth=0.7, linestyle='--')       # Her setter vi koden for streken på horensontal akse (axh) ved Y = 0, farge, linjetykkelse og linjestil
plt.axvline(0, color='black', linewidth=0.7, linestyle='--')       # Her gjør vi det samme som over bare med på vertikal akse (axv)
plt.grid(True, linestyle='--', alpha=0.7)                          # Her definerer vi grid som true så den kommer frem, linjestil og alpha gjør den transparang, satt til 70%
plt.show()                                                         # plt.show er kommandoen for at grafen skal vises i programmering-miljøet
