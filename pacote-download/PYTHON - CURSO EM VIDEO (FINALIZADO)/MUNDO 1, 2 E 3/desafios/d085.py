# DESAFIO 085 - Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


valores = [[],[]]
valor = 0

for c in range (0,7):
    valor = int(input(f'Digite o {c+1}º número: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)


valores[0].sort()
valores[1].sort()

print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

#corrigido
