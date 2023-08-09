# super() é a classe na sub classe
# Classe principal (Pessoa)
# -> super class, base class, parente class
# Classes filhas (Cliente)
# -> sub class, child class, derived class

class MinhaString(str):
    ...

string = MinhaString('Fernando')
print(string.upper())