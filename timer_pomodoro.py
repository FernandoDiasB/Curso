import time

def timer(segundos):
    while segundos > 0:
        print(f'Tempo restante {segundos} segundos')
        time.sleep(1)
        segundos -= 1
    print('Tempo esgotado')

tempo = int(input('Digite o tempo em que deseja manter o foco: '))
timer(tempo)