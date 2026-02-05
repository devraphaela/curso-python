# DESAFIO 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag = 999).

num = 0 
qtde_num = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: '))
    if num!= 999:
        qtde_num += 1
        soma += num
print(f'Você digitou {qtde_num} números e a soma deles é de {soma}')

#corrigido