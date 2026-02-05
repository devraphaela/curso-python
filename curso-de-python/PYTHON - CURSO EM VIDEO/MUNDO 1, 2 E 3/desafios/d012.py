#DESAFIO 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Digite o preço:'))
desc = preco * 0.05
novopreco = preco - desc

print ('O preço original é de R${:.2f}, com o desconto aplicado de 5%, o valor a pagar será de R${:.2f}'.format(preco,novopreco))

 #CORRIGIDO