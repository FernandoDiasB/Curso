import time
from os import system
import sys


def menu():
    print('###########Bem vindo(a)###############')
    opcao = input('Digite [1] para iniciar ou [2 para sair]: ')
    return opcao
   
while True:
    opcao = menu()
    if opcao == '1':
         break
    if opcao == '2':
        sys.exit()
    else:
        print('Digite apenas 1 ou 2')
        continue

        

class TimerPomo:
    def __init__(self, numero_ciclos, tempo_trabalho, tempo_descanso_curto, tempo_descanso_longo):
        self.numero_ciclos = numero_ciclos
        self.tempo_trabalho = tempo_trabalho
        self.tempo_descanso_curto = tempo_descanso_curto
        self.tempo_descanso_longo = tempo_descanso_longo


    def filtros(self):
        for ciclo in range(self.numero_ciclos):
            system('cls')
            print('Hora de trabalhar')
            self.timer(self.tempo_trabalho )
            


            if ciclo < numero_ciclos -1:
                    system('cls')
                    print('Descanso curto, aproveite para relaxar')
                    self.timer(tempo_descanso_curto )
            else:
                    system('cls')
                    print('Descanso longo, desliga um pouco e volte mais focado(a)')    
                    self.timer(tempo_descanso_longo )
                    menu()
                    
    

    def timer(self, t):
        
        while t:
            mins, secs = divmod(t, 60)
            contador = '{:02d}:{:02d}'.format(mins, secs)
            print(contador, end="\r")
            time.sleep(1)
            t -= 1


if __name__ == '__main__':
    numero_ciclos = 4
    tempo_trabalho = 10
    tempo_descanso_curto =5
    tempo_descanso_longo = 8

tempo = TimerPomo(numero_ciclos, tempo_trabalho, tempo_descanso_curto, tempo_descanso_longo)
tempo.filtros()