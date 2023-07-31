"""string = 'Fernando'
print(string.upper())
print(isinstance(string, str))"""

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Fernando','Dias')
#p1.nome = 'Fernando'
#p1.sobrenome = 'Dias'

p2 = Pessoa('Valentina','Almeida')
#p2.nome = 'Valentina'
#p2.sobrenome = 'Almeida'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)