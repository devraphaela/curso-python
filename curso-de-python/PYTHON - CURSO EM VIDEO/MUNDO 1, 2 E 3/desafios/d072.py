# DESAFIO 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

# Seu programa deverá ler o número pelo teclado (entre 0 e 20) e mostrar por extenso.

nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))

while True:
    print('Número inválido')
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break

for cont in range(0, len(nums)):
    if num == cont:
        print(f'Você digitou o número {nums[cont]}.')

#corrigido
    
    

