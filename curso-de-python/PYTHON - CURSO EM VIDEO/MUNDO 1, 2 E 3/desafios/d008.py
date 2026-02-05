#DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Digite o valor em metros:'))
cm = int(m *100)
mm = int(m *1000)

print('Seu valor em metros é de {}m, convertido para centímetros o resultado é {}cm, e convertido em milímetros é {}mm'.format(m, cm, mm))


 #CORRIGIDO