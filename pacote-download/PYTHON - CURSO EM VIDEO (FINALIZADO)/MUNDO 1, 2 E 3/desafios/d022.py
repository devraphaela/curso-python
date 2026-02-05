# DESAFIO 022 - Crie um programa que leia o nome completo de uma pessoa e mostre: 

# O nome com todas as letras maiúsculas 
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome 


# RESOLUÇÃO 

# Leia o nome completo de uma pessoa
nome = str(input('Digite o seu nome completo:'))

# O nome com todas as letras maiúsculas 
print('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))

# O nome com todas as letras minúsculas
print('Seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))

# Quantas letras ao todo (sem considerar os espaços)
print('O seu nome completo tem {} letras.'.format(len(nome.replace(" ", ""))))

# Quantas letras tem o primeiro nome
primeiro = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(primeiro[0], len(primeiro[0])))


# CORRIGIDO


