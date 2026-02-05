# DESAFIO 096 - Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a area do terreno.


def area(l, c):
    aTotal = l * c
    print(f'A área de um terreno {l}x{c} é de {aTotal}')


print('Controle de Terrenos')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)

#corrigido