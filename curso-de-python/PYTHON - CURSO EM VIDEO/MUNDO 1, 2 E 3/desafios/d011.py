#DESAFIO 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.

larg = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
area = larg * alt
print('area de {}'.format(area))

tinta = area /2 