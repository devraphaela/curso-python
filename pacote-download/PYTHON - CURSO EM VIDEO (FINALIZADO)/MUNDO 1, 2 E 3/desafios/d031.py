# DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem cobrando 0,50 por km para viagens até 200km e 0,45 para viagens mais longas 


# Desenvolva um programa que pergunte a distância de uma viagem em km
nome = str(input('Olá somos da agência de viagens TRANSBUS! Poderia nos informar o seu nome? '))
dist = float(input('Bem vindo(a) {}! nos informe a distância da sua viagem (em km):'.format(nome))) 

if dist <= 200:
    sempromo = dist * 0.50
    print('{}, sua viagem ficará R${:.2f}!'.format(nome,sempromo))
else:
    compromo = dist * 0.45
    print('{}, sua viagem ficará R${:.2f}!'.format(nome,compromo))
print('Boa viagem, obrigada por confiar na TRANSBUS!')


# corrigido