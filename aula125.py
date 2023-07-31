# Atributos de classe

class Pessoa:
    ano_atual = 'valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return 2023 - self.idade
    

p1 = Pessoa('Fernando', 30)
p2 = Pessoa('Valentina', 28)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())