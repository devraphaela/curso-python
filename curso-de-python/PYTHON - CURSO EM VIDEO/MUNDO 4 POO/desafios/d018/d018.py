# DESAFIO 018 - Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# Considere 
# consumo padrão por pessoa = 400g
# preço = R$82,40/Kg

from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__ (self, n, p):
        self.nome = n
        self.pessoas = p

    def analisar(self):

        qtdeporPessoa = 0.4
        precoCarne = 82.40
        totalCarne = self.pessoas * qtdeporPessoa
        totalPreco = precoCarne * totalCarne
        precoporPessoa = totalPreco / self.pessoas

        texto = f"Analisando [green]{self.nome}[/] com [blue]{self.pessoas} convidados[/] \nCada participante comerá {qtdeporPessoa}Kg e cada Kg custa R${precoCarne:.2f} \nRecomendo [blue]comprar {totalCarne:.3f}Kg[/] de carne \nO custo total será de [green]R${totalPreco:.2f}[/] \nCada pessoa pagará [yellow]R${precoporPessoa}[/] para participar."

        painel = Panel(texto, title = f'{self.nome}')

        print(painel)




c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()