# DESAFIO 022 - Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)

from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 10
        self.max_canais = 5

    def comando(self, tecla):
        if tecla == '@':
            self.ligado = not self.ligado
            print('TV ligada' if self.ligado else 'TV desligada')
            return

        if not self.ligado:
            texto2 = print('TV desligada - ligue com @')
            painel_desligado = Panel(texto2, title= '[TV]')
            return
        
        if tecla == '>':
            self.canal += 1
            if self.canal > self.max_canais:
                self.canal = 1
            print(f'Canal: {self.canal}')
        
        elif tecla == '<':
            self.canal -= 1
            if self.canal < 1:
                self.canal = self.max_canais
            print(f'Canal: {self.canal}')

        elif tecla == '+':
            self.volume += 1
            print(f'Volume: {self.volume}')

        elif tecla == '-':
            self.volume -= 1
            print(f'Volume: {self.volume}')

        else:
            print('[red]Comando inválido, digite novamente![/]')


controle = ControleRemoto()

print('Comandos: \n@ = liga/desliga \n< > canal \n+ - volume \n0 sair')

while True:
    tecla = input(' ')

    if tecla == '0':
        print('Encerrado')
        break

    controle.comando(tecla)