#Oppgave 2

#Programmet finner enten energien, farten eller massen til et legeme dersom de andre variablene er oppgitt

#Importerer math for å kunne bruke kvadratrot

import math

#Spør brukeren hvilken variabel han/hun ønsker å finne. Vi bryr oss ikke om det er stor eller liten bokstav, så vi bruker str.lower()
finneVariabel = str.lower(input("Hvilken variabel øsnker du å finne? E, m eller v?"))

#definerer alle variablene blankt for å kunne printe de senere
masse = 0
fart = 0
energi = 0

#Spør om de 2 andre variablene og regner ut variablene man ønsker og finne med formelen for kinetisk energi i et legeme
if(finneVariabel == "e"):
    masse = float(input("hva er massen i kg?"))
    fart = float(input("hva er farten i m/s?"))
    energi = (1/2)*masse*fart**2
    print()
elif(finneVariabel == "m"):
    energi = float(input("hva er energien i J?"))
    fart = float(input("hva er farten i m/s?"))
    masse = 2*(energi/fart**2)
elif(finneVariabel == "v"):
    energi = float(input("hva er energien i J?"))
    masse = float(input("hva er massen i kg?"))
    fart = math.sqrt(2*energi/masse)
else:
#Dersom variabelen brukeren oppga at de var ute etter ikke blir funnet, printer vi at den er ugyldig
    print("Ugyldig variabel")

#Printer resultatet med kontekst
print("Energi: " + str(energi) + "J")
print("Fart: " + str(fart) + "m/s")
print("Masse: " + str(masse) + "kg")