# DESAFIO 081 - Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

valores = []


print('Vamos começar!')

while True:
    num = int(input('Digite um número: '))
    valores.append(num)
 
    while True:
        perg = str(input('Você quer continuar? [S/N]').upper().strip())
        if perg in ('S', 'N'):
            break
        print('Resposta inválida, digite somente S ou N.')
    if perg != 'S':
        break

print(f'Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi digitado, então não faz parte da lista.')

#corrigido


        