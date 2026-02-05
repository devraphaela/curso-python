# DESAFIO 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

#ex: n = leiaInt('Digite um n')


def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('Erro! Digite um número válido')


# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


#corrigido