# DESAFIO 016 - Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, trabalho no setor de {self.setor} e meu cargo é {self.cargo}."
    

# Exemplo de uso    
funcionario1 = Funcionario("Raphaela", "TI", "Desenvolvedora")
print(funcionario1.apresentar())

funcionario2 = Funcionario("Carlos", "Recursos Humanos", "Analista")
print(funcionario2.apresentar())