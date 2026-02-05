# DESAFIO 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


num = 0
pergunta = 0
qtde_num = 0
soma = 0

while pergunta != 'N':
    num = int(input('Digite um valor: '))
    pergunta = str(input('Você quer continuar digitando mais valores? [S/N]: ')).upper().strip()
    qtde_num += 1
    soma += num
    
    if num == 1: # primeiro numero digitado
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num

media = soma / qtde_num

print('Já que você não quer digitar mais valores, aqui vão alguns cálculos que eu fiz:')
print(f'A média dos números que você digitou é de {media:.1f}')
print(f'Já o maior valor lido foi {maior} e o menor valor lido foi {menor}')

#corrigido