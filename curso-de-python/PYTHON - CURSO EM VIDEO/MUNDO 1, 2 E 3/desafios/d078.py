# DESAFIO 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista

valores = []
maior = 0
menor = 0
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Voce digitou os valores {valores}')

print(f'O maior valor foi {maior}, nas posições: ' , end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}..')

print(f'O menor valor foi {menor}, nas posições: ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}..')
        


#corrigido
