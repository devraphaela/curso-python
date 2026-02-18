# DESAFIO 021 - Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.

from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True

        if cor == 'azul':
            self.cor_rich = 'blue'
        elif cor == 'vermelha' or cor == 'vermelho':
            self.cor_rich = 'red'
        elif cor == 'verde':
            self.cor_rich = 'green'
        elif cor == 'amarela' or cor == 'amarelo':
            self.cor_rich = 'yellow'
        elif cor == 'preta'or cor == 'preto':
            self.cor_rich = 'black'
        else:
            self.cor_rich = 'white'
        

    def destampar(self):
        self.tampada = False
    
    
    def escrever(self, texto): 
        if self.tampada:
            print('A caneta está tampada!!!')
        else:
            print(f'[{self.cor_rich}]{texto}[/]')


    def quebrar_linha(self, qtd):
        print('\n' * qtd, end='')



c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)
c2.escrever('Olá Gafanhoto! ')
c3.escrever('Vamos exercitar!')
