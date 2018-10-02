
#Oppgave 4

#Programmet finner n!, med variabelen n oppgitt

#Importerer math for å kunne runde av til nærmeste heltall
import math

#Spør brukeren om et positivt heltall n. Unngår å runde det til nærmeste heltall, slik at vi kan sjekke om brukeren faktisk oppga et heltall senere
n = float(input("Oppgi et positivt heltall "))

#Sjekker om det oppgitte tallet er et heltall og positivt. Hvis ikke gir vi feilmelding 
if(n == round(n) and n >= 0):
    #Regner ut fakultet  ved å gange heltallet med alle tallene fra 1 til og med seg selv. Caster n om til int, fordi vi vet at det er et heltall
    fakultet = 1
    for i in range(1, int(n) + 1):
        fakultet *= i
    #Printer svaret med kontekst
    print("Oppgitt tall: " + str(int(n)))
    print("Fakultet: " + str(fakultet))
else:
    print("n er ikke et positivt heltall!")