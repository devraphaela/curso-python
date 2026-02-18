# DESAFIO 020 - Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favs = []
        
        

    def add_favoritos(self, jogo):
        self.favs.append(jogo)

    def ficha(self):
        if self.favs:
            jogos_texto = ""
            for jogo in sorted(self.favs):
                jogos_texto += f':video_game: [blue]{jogo}\n'
        else:
            jogos_texto = 'Nenhum'

        texto = f'Nome real: [bold black on blue]{self.nome}[/] \nJogos favoritos: \n{jogos_texto}'
        painel = Panel(texto, title=f'Jogador <{self.nick}>', width=40)

        print(painel)



j1 = Gamer ('Fabrício da Silva', 'detonador2025')
j1.add_favoritos('Mario Bros.')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_favoritos('Mario Bros.')
j2.add_favoritos('Call of Dudy')
j2.add_favoritos('Valorant')
j2.ficha()
