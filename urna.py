import random
from bola import Bola

class Urna:
    def __init__(self):
        self.bolas = [Bola(numero) for numero in range(1, 21)]

    def sortear_bola(self):
        indice_aleatorio = random.randrange(len(self.bolas))
        bola_sorteada = self.bolas.pop(indice_aleatorio)
        return bola_sorteada

    def recolocar_bola(self, bola):
        self.bolas.append(bola)