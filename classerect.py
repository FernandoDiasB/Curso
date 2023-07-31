class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarDados(self, comp2, larg2):
        self.comprimento = comp2
        self.largura = larg2
    
    def retornarLados(self):
        return self.comprimento, self.largura

    def calculoArea(self):
        return comprimento * largura
    
    def perimetro(self):
        return (comprimento + largura) * 2



comprimento = int(input('digite o comprimento desejado em metro: '))
largura = int(input('digite a largura desejada em metro: '))

medidas = Retangulo(comprimento, largura)

print(f'As mediadas digitadas foram: {medidas.retornarLados()}')
print(f'A área total de piso será: {medidas.calculoArea()}m²')
print(f'O perimetro total de rodapés em metros lineares é de: {medidas.perimetro()}m')

