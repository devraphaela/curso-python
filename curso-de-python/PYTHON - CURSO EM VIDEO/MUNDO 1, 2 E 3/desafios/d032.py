# DESAFIO 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

# programa que leia um ano qualquer
ano = int(input('Digite um ano para saber se ele é bissexto ou coloque 0 para checar o ano atual: '))
if ano == 0:
    ano = date.today().year

# mostre se ele é bissexto.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))

# corrigido