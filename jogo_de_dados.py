import random


class Dado():
    def __init__(self, info1):
        self.info1 = info1


    def aleatorio():
        return random.randint(1, 6)

numero = Dado.aleatorio()


while True:

    escolha = int(input('Digite um valor: '))
    if escolha not in range(1,7):
        print('Lembre-se que os dados vão de 1 a 6.')
        continue

    elif escolha != numero:
        print('Tente novamente!')
    
    else:
        print('Parabens!\nVocê Acertou')
        break


        