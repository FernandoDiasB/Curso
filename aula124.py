class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está fimando')
            return

        print(f'{self.nome} Está parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')
        self.fotografando = True
        

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.parar_de_filmar()
c1.fotografar()
print(c1.filmando)
print(c2.filmando)