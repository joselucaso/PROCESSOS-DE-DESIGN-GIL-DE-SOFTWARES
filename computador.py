from urna import Urna

class Computador:
    def __init__(self, jogo):
        self.jogo = jogo
        self.alvo = None

    def definir_alvo_inicial(self):
        bola_sorteada = self.jogo.urna.sortear_bola()
        self.alvo = bola_sorteada.numero
        self.jogo.urna.recolocar_bola(bola_sorteada)

    def definir_alvo_subsequente(self, bola):
        self.alvo += bola.numero

    def informar_alvo(self):
        print("O alvo é:", self.alvo)