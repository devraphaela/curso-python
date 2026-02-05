# DESAFIO 023 - Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# EX: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1



#RESOLUÇÃO

# Leia de 0 a 9999
num = int(input('Digite um número de 0 até 9999: '))

# Forma matemática de pegar cada um
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Mostrar na tela cada um dos dígitos separados
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# CORRIGIDO

