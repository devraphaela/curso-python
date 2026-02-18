# DESAFIO 018 - Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# Considere 
# consumo padrão por pessoa = 400g
# preço = R$82,40/Kg

from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__ (self, nome, pessoas, qtde_por_pessoa=0.4, preco_carne=82.40):
        self.nome = nome
        self.pessoas = pessoas
        self.qtde_por_pessoa = qtde_por_pessoa
        self.preco_carne = preco_carne

    def analisar(self):

        total_carne = self.pessoas * self.qtde_por_pessoa
        total_preco = self.preco_carne * total_carne
        preco_por_pessoa = total_preco / self.pessoas

        texto = f"Analisando [green]{self.nome}[/] com [blue]{self.pessoas} convidados[/] \nCada participante comerá {self.qtde_por_pessoa}Kg e cada Kg custa R${self.preco_carne:.2f} \nRecomendo [blue]comprar {total_carne:.3f}Kg[/] de carne \nO custo total será de [green]R${total_preco:.2f}[/] \nCada pessoa pagará [yellow]R${preco_por_pessoa:.2f}[/] para participar."

        painel = Panel(texto, title = f'{self.nome}')

        print(painel)




c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()