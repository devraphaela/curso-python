# DESAFIO 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

# Qual é o total gasto na compra
# Quantos produtos custam mais de R$ 1.000,00
# Qual é o nome do produto mais barato

print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)

total = 0
maior_Mil = 0
mais_Barato = 0
nome_Mais_Barato = ''

while True:
    nome_Prod = str(input('Nome do produto: '))
    preco_Prod = int(input('Preço do produto: R$'))
    total += preco_Prod
   
    if preco_Prod >= 1000:
        maior_Mil += 1

    if mais_Barato == 0:
        mais_Barato = preco_Prod
        nome_Mais_Barato = nome_Prod
    elif preco_Prod < mais_Barato:
        mais_Barato = preco_Prod
        nome_Mais_Barato = nome_Prod
    
    perg = str(input('Quer continuar? [S/N] ')).lower().strip()
    if perg != 's':
        break

print(f'O total gasto foi de R${total}.')    
print(f'{maior_Mil} produtos da sua lista custam mais de R$1000.')
print(f'E o produto mais barato da sua lista é {nome_Mais_Barato}, custando R${mais_Barato}.')

#corrigido