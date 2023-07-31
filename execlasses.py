"""class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor



ball = Bola('Vermelha', 25, 'Plástico')

print(f'A bola é {ball.mostraCor()}, tem {ball.circunferencia} cm de diâmetro e é feita de {ball.material}')
print()

ball.trocaCor('Roxa')
print(f'A bola é {ball.mostraCor()}, tem {ball.circunferencia} cm de diâmetro e é feita de {ball.material}')
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarValor(self, valor):
        self.lado = valor

    def mostraValor(self):
        return self.lado


medida = Quadrado(10)

print(f'O quadrado tem {medida.mostraValor()}cm de largura e altura')
print()
medida.mudarValor(15)
print(f'O quadrado tem {medida.mostraValor()}cm de largura e altura')
