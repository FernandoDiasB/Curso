class Conta:
    def __init__(self, conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, nome1):
        self.nome = nome1

    def saque1(self, saque):
        self.saque = saque
        return saque
    
    def deposito1(self, deposito):
        self.deposito = deposito



while True:

    nome = input('Digite seu nome: ')
    conta = int(input('Digite o nomero da conta: '))
    saldo_inicial = 0
    

    
    
    if nome != 'Fernando Dias':
        continue
    else:
        break

saldo = saldo_inicial
dados = Conta(conta, nome, saldo)


print('Menu:')
print('1 - Depósito')
print('2 - Saque')
print('3 - saldo')
print('4 - Sair')
op1 = int(input('Digite a opção desejada: '))


if op1 == 1:
    deposito = int(input('digite o valor que irá depositar: '))

    print(f'Você depositou {deposito}')
    print(f'O saldo da sua conta é: {dados.saldo + deposito}')



