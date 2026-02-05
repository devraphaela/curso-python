# DESAFIO 055 - Faça um programa que leia o peso de 5 pessoas, e mostre qual foi o maior e o menor peso lidos.



for c in range (0,5):
    peso = float(input('Digite o seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso



print(f'o maior peso é de {maior} e o menor peso é de {menor}')

#CORRIGIDO