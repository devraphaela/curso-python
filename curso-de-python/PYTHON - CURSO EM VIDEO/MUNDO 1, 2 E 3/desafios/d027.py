# DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.

# EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza


# RESOLUÇÃO

# Leia o nome completo de uma pessoa
nome = str(input('Digite o seu nome completo:')).strip()

# Separar nomes
nomes = (nome.split())

# Primeiro nome
print('Seu primeiro nome é: {}'.format(nomes[0]))

# Último nome
print('Seu último nome é: {}'.format(nomes[len(nomes)-1]))

# CORRIGIDO

