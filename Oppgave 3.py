
#Oppgave 3

#Programmet finner dyrebefolkningen etter t år

#Spør brukeren om variablene vi trenger
B_Gammel = float(input("Hva er den nåværende befolkningen? "))
t = int(input("antall år senere "))
p = float(input("Vekst (i prosent, absoluttverdi) "))

#Spør brukeren om befolkningen øker/synker, og justerer vekstfaktoren deretter
økende = str(input("øker befolkningen? ja/nei "))
if(økende == "nei"):
    p = -p

#Definerer den nye befolkningen som lik den gamle til å starte med
B_Ny = B_Gammel

#Iterer for hvert år og senker/øker befolkningen
for år in range(t):
    B_Ny *= 1 + (p/100)

#Printer den nye befolkningen med kontekst
print("Gammel befolkning: " + str(B_Gammel))
print("Antall år: " + str(t))
print("Vekst (i prosent, absoluttverdi): " + str(p))
print("Ny befolkning: " + str(B_Ny))
