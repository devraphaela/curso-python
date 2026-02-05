#DESAFIO 013 - Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o seu salário:'))
aumento = salario * 0.15
novosalario = float(salario + aumento)

print('O seu salário era de R${}, agora com o aumento de 15%, seu novo salário será de R${:.2f}'.format(salario,novosalario))

 #CORRIGIDO