
#DESAFIO 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

# 1 modo
nome = str(input('Digite o seu nome:'))

print('Olá', nome,'!','Prazer em te conhecer.')


# 2 modo com .format
nome = str(input('Digite o seu nome:'))

print('Olá {}! Prazer em te conhecer.'.format(nome))




#DESAFIO 002 - Crie um programa que leia dois números e mostre a soma entre eles

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
soma = num1 + num2

print('A soma vale', soma)