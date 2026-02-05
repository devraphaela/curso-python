# AULA 04 - Criando Classes e Objetos na Prática

# Qual é a diferença entre objeto e variável?
# Quando vamos colocar a mão na massa?
# Como faço para declarar uma classe?
# Como instanciar um objeto a partir de uma classe?

# "Objetos são variáveis evoluídas."

# variaveis compostas e funções estavam em lugares separados 
    # dados separados de funções

# Objeto é uma variável que além de guardar dados, podem fazer coisas com esses dados (dados(atributo) + funções(metodo))





# PRÁTICA

# declaração da classe (definição)
class Gafanhoto:
    def __init__(self): #metodo construtor
        # atributos de instância
        self.nome = ""
        self.idade = 0

    # metodos de instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# declaração dos objetos (execução)
g1 = Gafanhoto() # parenteses = chamam para instanciar, vc chama um método construtor (def__init__(self):)       # g1 = objeto           # self= nome generico do OBJETO que chamou
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mario'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())