#Esercizio 1
età=int(input("Quanti anni hai?"))
patente=input("Hai la patente? si/no ")
risposta= età>= 18 and patente=="si"
print(risposta)

#Esercizio 2
Ritardo= input("L'utente è in ritardo con la restituzione? si/no ")
Premium= input("L'utente ha un abbonamento premium? si/no ")
print(Ritardo== "no" or Premium== "si" )