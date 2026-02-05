# DESAFIO 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não são maiores de idade e quantas ja são.
# dessas tantas pessoas x atingiram e y nao 21 anos

from datetime import date


menorDeIdade = 0
maiorDeIdade = 0
anoAtual = date.today().year

# programa que leia o ano de nascimento de sete pessoas
for c in range (0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = anoAtual - nasc 
    if idade < 21:
        menorDeIdade += 1
    else:
        maiorDeIdade += 1

print(f'Nesse grupo existem {menorDeIdade} pessoas que ainda não atingiram a maioridade e {maiorDeIdade} pessoas que já antingiram a maioridade.')

#CORRIGIDO