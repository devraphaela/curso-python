# DESAFIO 050 - Faça um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.

soma = 0
cont = 0
for c in range(0,6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        cont += 1
        soma += num   
        
print(f'Voce informou {cont} números pares e a soma dos números pares é de: {soma}')

#CORRIGIDO