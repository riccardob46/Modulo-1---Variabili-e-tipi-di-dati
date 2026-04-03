#ESERCIZIO FINE VIDEOLEZIONE
#1
class Divisione:
    def dividi(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Divisione per 0 non consentita!"
calc= Divisione()
risultato= calc.dividi(10, 2)
print(risultato)

#2
class Persona:
    def __init__(self, nome, età):
        if età < 0:
            raise ValueError("L'età inserita è negativa")
        self.nome= nome
        self.età= età
    def __str__(self):
        return f"Persona: {self.nome}, Età: {self.età}"
p= Persona("Luca", 25)
print(p)
p2= Persona("Marco", 16)
print(p2)

#3
class InsufficientBalanceError(Exception):
    pass
class Banca:
    def __init__(self, saldo):
        self._saldo= saldo
        
    def prelievo(self, importo):
        if importo > self._saldo:
            raise InsufficientBalanceError("Prelievo non disponibile per Saldo Insufficiente!")
        self._saldo -=importo

conto= Banca(1500)
prelievo= conto.prelievo(600)
print(f"Saldo finale: {conto._saldo}")
