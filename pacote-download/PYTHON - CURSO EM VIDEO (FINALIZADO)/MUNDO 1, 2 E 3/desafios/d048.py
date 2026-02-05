# DESAFIO 048 - Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 a 500.

soma = 0 
cont = 0

for c in range(1, 501, 2):
    if c % 2 != 0 and c % 3 == 0:
        cont += 1 #contador // cont = cont + 1
        soma += c #acumulador // soma = soma + c


print(f'Total de {cont} valores:', soma)

#corrigido