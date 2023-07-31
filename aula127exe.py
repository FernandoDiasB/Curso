"""
Salve sua classe em JSON
Salve os dados da sua classe em JSON
Crie novamente as instâncias da classe com os dados salvos
"""

import json

CAMINHO_ARQUIVO = 'aula127exe.json'


class Carro:
    def __init__(self, nome, cor, ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano


veiculo1 = Carro('TR4', 'Cinza', 2015)
veiculo2 = Carro('Civic', 'Preto', 2014)
bd = [vars(veiculo1), vars(veiculo2)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)




"""
print(f'O carro que a Valentina terá é um {veiculo1.nome}, a cor mais bonita é o {veiculo1.cor} e possivelmente o ano será {veiculo1.ano}')
print(vars(veiculo1))
print()
print(f'O carro que a Fernando terá é um {veiculo2.nome}, a cor mais bonita é o {veiculo2.cor} e possivelmente o ano será {veiculo2.ano}')
print(vars(veiculo2))
"""