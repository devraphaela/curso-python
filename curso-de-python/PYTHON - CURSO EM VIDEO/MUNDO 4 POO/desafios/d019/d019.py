# DESAFIO 019 - Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.

from rich import print

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1

        print(f'[blue]Você acabou de abrir o livro[/] [bold red]"{self.titulo}"[/] [blue]que tem[/] [bold green]{self.total_paginas} páginas[/] [blue]no total. Você agora está na[/] [bold yellow]página {self.pagina_atual}[/]')
  
    def avancar_paginas(self, n=1):
        if self.pagina_atual + n > self.total_paginas:
            n = self.total_paginas - self.pagina_atual

        self.pagina_atual += n

        if self.pagina_atual >= self.total_paginas:
            self.pagina_atual = self.total_paginas
            print(f'[blue]Você avançou [bold]{n}[/] páginas e agora está na [/][yellow]página[bold] {self.pagina_atual}[/] \n[red]Você chegou ao final do livro {self.titulo}[/]')
        else:
            print(f'[blue]Você avançou {n} páginas e agora está na [/] [yellow]página {self.pagina_atual}[/]')



l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)