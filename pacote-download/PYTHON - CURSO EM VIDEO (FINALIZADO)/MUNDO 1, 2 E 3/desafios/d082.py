# DESAFIO 082 - Crie um programa que vai ler vários números e colocar em uma lista. 

# Depois disso, cire duas listas extras que vao conter apenas os valores pares e os valores ímpares digitados respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

valores = []
valores_Par = []
valores_Impar = []

while True:
    num = int(input('Digite um número: '))

    if num not in valores:
         valores.append(num)
    else:
        print(f'O número {num} já foi digitado, tente outro número.')

    while True:
        perg = str(input('Quer continuar? [S/N]')).upper().strip()
        if perg in ('S', 'N'):
            break
        ('Resposta inválida, digite somente S ou N.')

    if perg != 'S':
        break


for v in valores:
    if v % 2 == 0:
        valores_Par.append(v)
    else:
        valores_Impar.append(v)

print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {valores_Par}')
print(f'A lista de ímpares é: {valores_Impar}')


#corrigido



