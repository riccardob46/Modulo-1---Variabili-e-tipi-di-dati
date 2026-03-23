scelta_frase=input('Digita una frase')

#inversione parole
parole=scelta_frase.split()
inverse=parole[::-1]
risultato="".join(inverse)
print(risultato)

#verifica palindromo
pulizia_frase=scelta_frase.lower().replace(" ", "")
inversione= pulizia_frase[::-1]
if inversione == pulizia_frase:
    print('Si è un palindromo')
else:
    print('no, non è un palindromo')    
