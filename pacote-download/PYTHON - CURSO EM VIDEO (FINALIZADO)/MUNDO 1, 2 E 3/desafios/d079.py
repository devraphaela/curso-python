# DESAFIO 079 - Crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


valores = list()

print('Vamos coletar alguns números!')

while True:
    num = int(input('Digite um número: '))

    if num not in valores:
        valores.append(num)
    else:
        print(f'o número {num} já foi digitado, tente outro!')
         
    while True:
        perg = str(input('Quer continuar? [S/N]')).upper().strip()
        if perg in ('S', 'N'):
            break
        print('Resposta inválida! Digite apenas S ou N.')
        
    if perg != 'S':
        break

valores.sort()
print(f'Os valores que você digitou foram: {valores}')

#corrigido