class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorAbastecido):
        qtdAbastecida = valorAbastecido / self.valorLitro
        if qtdAbastecida <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= qtdAbastecida
            print(f'Foram abasteidos: {qtdAbastecida:.2f} litros')
        else:
            print('Combustível insuficiente')


    def abastecerPorLitro(self, litroAbastecido):
        valorAbastecido1 = litroAbastecido * self.valorLitro
        if litroAbastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litroAbastecido
            print(f'Voce abasteceu um total de R$ {valorAbastecido1:.8}')
        else:
            print('Combustível insuficiente')
        
    def alterarValor(self, newValor):
        self.valorLitro = newValor
        print(f'O valor com reajuste é: {self.valorLitro}')

    def alterarCombustivel(self, newCombustivel):
        self.tipoCombustivel = newCombustivel
        print(f'O combustível foi alterado para {self.tipoCombustivel}')
    
    def alterarQuantidadeCombustivel(self, CombustivelNaBomba):
        self.quantidadeCombustivel = CombustivelNaBomba
        print(f'Total restante na bomba: {self.quantidadeCombustivel}')


bomba = bombaCombustivel('Gasolina', 5.75, 100)
bomba.abastecerPorValor(150)
bomba.abastecerPorLitro(21)
bomba.alterarValor(5.30)
bomba.alterarQuantidadeCombustivel(99)