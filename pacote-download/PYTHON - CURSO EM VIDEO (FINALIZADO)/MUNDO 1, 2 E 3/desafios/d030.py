# DESAFIO 030 - Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar

# if divisivel por..


# programa que leia um número inteiro qualquer
nome = str(input('Digite o seu nome:'))
print('Olá {}, vamos verificar se um número é par ou ímpar.'.format(nome))
num = int(input('Por favor digite um número:'))

# mostre na tela se ele é par ou ímpar
if num % 2 == 0:
    print('{}, o número {} é par!'.format(nome,num))
else:
    print('{}, o número {} é ímpar!'.format(nome,num))


# corrigido