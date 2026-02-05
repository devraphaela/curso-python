# DESAFIO 038 - Escreva um programa que leia dois numeros inteiros e compare mostrando na tela uma mensagem
# o primeiro valor é maior 
# o segundo valor é maior
# não existe valor maior, os dois são iguais 

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
maior = n1

if n2 > maior:
    print('O segundo número é maior!')
elif maior == n2:
    print('Não existe número maior, os dois são iguais.')
else:
    print('O primeiro número é maior!')

#corrigido