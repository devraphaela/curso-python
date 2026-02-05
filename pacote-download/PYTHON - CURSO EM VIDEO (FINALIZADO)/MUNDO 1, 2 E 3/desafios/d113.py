# DESAFIO 113 - Reecreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            valorInt = int(input(msg))
        except(ValueError, TypeError):
            print('Erro! Digite um número válido')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar o valor.')
            return 0
        else:
            return valorInt

def leiaFloat(msg):
    while True:
        try:
            valorFloat = input(msg)
        except(ValueError, TypeError):
            print('Erro! Digite um número válido')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar o valor.')
            return 0.0
        else:
            return valorFloat


# programa principal
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')

print(f'O valor inteiro foi {i} e o valor real foi {f}')

#corrigido