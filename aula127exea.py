import json
from aula127exe import CAMINHO_ARQUIVO, Carro

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
#    print(dados)

    veiculo1 = Carro(**dados[0])
    veiculo2 = Carro(**dados[1])
    print(veiculo1.nome)
    print(veiculo2.cor)