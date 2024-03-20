class Jogador:
    def __init__(self):
        self.palpite = None

    def inserir_palpite(self):
        while True:
            try:
                self.palpite = int(input("Digite seu palpite (1 a 20): "))
                if 1 <= self.palpite <= 20:
                    break
                else:
                    print("Palpite inválido. Digite um número entre 1 e 20.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def receber_feedback(self, feedback):
        print(feedback)