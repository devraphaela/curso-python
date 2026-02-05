# DESAFIO 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "São"


#RESOLUÇÃO

# Leia o nome de uma cidade
cidade = str(input('Digite o nome de uma cidade:')).strip()

# Se ela começa ou não com o nome "São"
print(cidade[:4].upper() == 'São')


