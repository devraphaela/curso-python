# DESAFIO 087 - Aprimore o desafio anterior mostrando no final:

# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna
# O maior valor da segunda linha


matriz = list()
soma_Pares = 0
soma_Terceira = 0
maior = 0

for c in range (0,9):
    matriz.append(int(input('Digite um valor: ')))


matriz.sort()
print(f'[', matriz[0], ']', end='')
print(f'[', matriz[1], ']', end='')
print(f'[', matriz[2], ']')
print(f'[', matriz[3], ']', end='')
print(f'[', matriz[4], ']', end='')
print(f'[', matriz[5], ']')
print(f'[', matriz[6], ']', end='')
print(f'[', matriz[7], ']', end='')
print(f'[', matriz[8], ']')

for n in matriz:
    if n % 2 == 0:
        soma_Pares += n

for n in matriz[2], matriz[5], matriz[8]:
    soma_Terceira +=n

for n in matriz[3], matriz[4], matriz[5]:
    if n == 0:
        maior = n
    else:
        if n > maior:
            maior = n

print(f'A soma dos valores pares é de {soma_Pares}')
print(f'A soma dos valores da terceira coluna é de {soma_Terceira}')
print(f'O maior valores da segunda linha é o {maior}')


#corrigido


