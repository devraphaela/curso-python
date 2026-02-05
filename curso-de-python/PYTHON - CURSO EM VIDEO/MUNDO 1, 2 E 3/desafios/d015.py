#DESAFIO 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtkm = float(input('Digite a quantidade de km percorridos:'))
qtdia = int(input('Digite a quantidade de dias que ele foi alugado:'))
dia = 60
km = 0.15

calculokm = qtkm * km
calculodia = qtdia * dia

total = calculodia + calculokm

print('Você alugou o carro por {} dias, e rodou com ele por {}km, então irá pagar R${:.2f}.'.format(qtdia,qtkm,total))