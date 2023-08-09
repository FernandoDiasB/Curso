# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
#Herança vs Composição
#
# Diretor de classe (Pessoa)
# -> superclasse, classe base, classe pai
# Aulas filhas (Cliente)
# -> subclasse, classe filha, classe derivada


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...

c1 = Cliente('Fernando', 'Dias')
c1.falar_nome_classe()
a1 = Aluno('Valentina', 'Almeida')
a1.falar_nome_classe()
help(Cliente)