class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano

    def informacoes(self):
        print(f'A cor do carro é {self.cor}')
        print(f'O ano do carro é {self.ano}')

    def ligar_desligar(self, ligar_desligar):
        if ligar_desligar == 'ligar':
            return 'Carro foi ligado'
        if ligar_desligar == 'desligar':
            return 'Carro foi desligado'
