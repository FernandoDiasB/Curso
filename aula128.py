# Métodos de classe + factories
# São métodos onde "self" será "cls", ou seja, 
# ao invés de receber a instânciano primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_classe(self):
        print('Hey')

p1 = Pessoa('Fernando', 30)

print(p1.nome, p1.idade)
Pessoa.metodo_de_classe(p1)