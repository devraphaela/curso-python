# DESAFIO 075 - Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

conj = ()
cont = 0
par = ()

for c in range(0,4):
    num = int(input('Digite um valor: '))
    conj += num,
    if num == 9:
        cont += 1
    if num % 2 == 0:
        par += num,


print('='*30)
print(f'Você digitou os valores: {conj}')

# Quantas vezes apareceu o valor 9
if cont > 0:
    print(f'O número 9 apareceu {cont} vezes.')
else:
    print('O número 9 não apareceu na sequência.')


# Em que posição foi digitado o primeiro valor 3
if 3 in conj:
    print(f'O número 3 foi digitado na {conj.index(3)+1}º posição')
else:
    print('O número 3 não foi digitado em nenhuma posição.')

# Quais foram os números pares
print(f'Os valores pares digitados foram {par}')

#corrigido