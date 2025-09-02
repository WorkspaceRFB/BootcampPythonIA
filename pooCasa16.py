class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrarCor(self):
        return(f'A cor da casa é {self.cor}.')

    def mostrarQuartos(self):
        return(f'Esta casa possui {self.quartos} quarto(s).')
    
    def mostrarBanheiros(self):
        return(f'Esta casa possui {self.quartos} banheiro(s).')
    
    def construirQuarto(self):
        self.quartos += 1
        return(f'Agora esta casa possui {self.quartos} quarto(s).')
    
    def pintarCasa(self, novaCor):
        self.cor = novaCor
        return(f'A atual cor dessa casa é {self.cor}.')