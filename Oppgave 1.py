#Oppgave 1

#Programmet finner pH-verdien til en løsning med oppgitt h+ion-konsentrasjon

#Importerer math for å bruke logaritmer
import math

#Ber brukeren skrive inn H+ konsentrasjonen
hPlussKonsentrasjon = float(input("Hvor mange H+ ioner er det i mol per liter?"))

#Regner ut pH-verdien med den generelle formelen for pH-skalaen. Må bruke log10() for å presisere at det er briggske logaritmer det er snakk om
pH = -math.log10(hPlussKonsentrasjon)

#Printer pH-verdien 
print("pH-verdi: " + str(pH))

#Finner ut om pH-verdien gjør løsningen basisk (7 < pH ≤ 14), nøytral (pH == 7) eller sur (0 ≤ pH < 7)
if(pH <= 14 and pH > 7):
    print("En basisk løsning")
elif(pH == 7):
    print("En nøytral løsning")
elif(pH >= 0):
    print("En sur løsning")