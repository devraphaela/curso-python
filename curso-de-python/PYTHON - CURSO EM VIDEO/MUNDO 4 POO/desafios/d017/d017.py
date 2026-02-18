# DESAFIO 017 - Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        
        preco_str = f"R${self.preco:,.2f}"

       
        largura_necessaria = max(len(self.nome), len(preco_str) + 20)  
        largura_panel = max(50, largura_necessaria)  

       
        linha_nome = self.nome.center(largura_panel - 4)

       
        linha_sep = "-" * (largura_panel - 7)
        linha_sep = linha_sep.center(largura_panel - 4)

       
        total_pontos = largura_panel - 6 - len(preco_str)
        pontos_esq = total_pontos // 2
        pontos_dir = total_pontos - pontos_esq
        linha_preco = "." * pontos_esq + preco_str + "." * pontos_dir

    
        texto = f"{linha_nome}\n{linha_sep}\n{linha_preco}"

        painel = Panel(texto, title="Produto", width=largura_panel, padding=(1,2))
        print(painel)



p1 = Produto('Iphone 17 Pro Max', 25000.85)
p2 = Produto('Mouse', 120)

p1.etiqueta()
p2.etiqueta()