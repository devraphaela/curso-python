# DESAFIO 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.


pacientes = list ()
dados = list ()
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(pacientes) == 0:
        maior = menor = dados[1] #guardando o peso como maior e menor
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
            
    pacientes.append(dados[:])
    dados.clear()

    p = str(input('Quer continuar? [S/N]')).upper().strip()
    if p != 'S':
        break

print(f'Foram cadastradas {len(pacientes)} pacientes.')

print(f'O maior peso foi de {maior:.2f}Kg. Peso de: ', end='')
for p in pacientes:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor:.2f}Kg. Peso de: ', end='')
for p in pacientes:
    if p[1] == menor:
        print(f'[{p[0]}]')

#corrigido


