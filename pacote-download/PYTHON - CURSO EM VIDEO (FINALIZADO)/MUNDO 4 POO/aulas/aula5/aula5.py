# AULA 05 - Melhorando Classes e Criando uma Conta Bancária na Prática.


# PRÁTICA

# declaração da classe (definição)
class Gafanhoto:
    """"
Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
Para criar uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): #metodo construtor
        # atributos de instância
        self.nome = nome
        self.idade = idade

    # metodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# declaração dos objetos (execução)
g1 = Gafanhoto('Maria', 17)           
g1.aniversario()
#print(g1) # Dunder Attribute
print(g1.__dict__) # exibição em forma de dicionário # atributo
print(g1.__getstate__()) # metodo
print(g1.__class__) # atributo com double underline
print(g1.__doc__)


# g2 = Gafanhoto('Mauro', 54)
# print(g2)
# print(g2.__getstate__)

# g3 = Gafanhoto()
# print(g3.mensagem())