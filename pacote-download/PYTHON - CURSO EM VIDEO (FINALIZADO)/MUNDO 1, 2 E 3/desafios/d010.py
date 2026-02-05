#DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quanto você tem na carteira:'))
cot = 3.27
dol = real / cot

print ('Sabendo que você tem R${}, e a cotação do dolar está em {}, você terá US${:.2f}'.format(real,cot,dol))


 #CORRIGIDO