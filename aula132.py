# @property + @setter - getter e setter no modo Pythonico como getter
# Evita quebrar o código cliente
# Habilitar o setter
# Executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor
    
def mostrar(caneta):
        return caneta.cor

    
caneta = Caneta('Azul')
print(caneta.cor)