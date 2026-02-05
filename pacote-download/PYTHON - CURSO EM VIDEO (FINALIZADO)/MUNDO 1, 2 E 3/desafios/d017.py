# DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

catoposto = int(input('Digite o cateto oposto:'))
catadjacente = int(input('Digite o cateto adjacente:'))


potoposto = math.pow(catoposto, 2)
potadjacente = math.pow(catadjacente, 2)

hipo = math.sqrt(potoposto + potadjacente)

print('A hipotenusa é {}'.format(hipo))

