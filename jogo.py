from urna import Urna
from jogador import Jogador
from computador import Computador

class Jogo:
    def __init__(self):
        self.urna = Urna()
        self.jogador = Jogador()
        self.computador = Computador(self)

    def iniciar_jogo(self):
        self.computador.definir_alvo_inicial()
        self.computador.informar_alvo()

    def gerenciar_jogadas(self):
        while True:
            # Jogador insere palpite
            self.jogador.inserir_palpite()

            # Avaliar palpite
            if self.jogador.palpite == self.computador.alvo:
                feedback = "Você acertou!"
                break
            else:
                feedback = "Você errou!"

            # Computador define novo alvo
            bola_sorteada = self.urna.sortear_bola()
            self.computador.definir_alvo_subsequente(bola_sorteada)
            self.urna.recolocar_bola(bola_sorteada)

            # Informar feedback e novo alvo
            self.jogador.receber_feedback(feedback)
            self.computador.informar_alvo()

            
    def exibir_mensagem_fim(self):
        print("Jogo encerrado!")


