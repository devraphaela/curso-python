# DESAFIO 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a 1.250,00 calcule um aumento de 10%

# Para os inferiores ou iguais, o aumento é de 15%

# programa que pergunte o salário de um funcionário 
nome = str(input('Digite o seu nome:'))
sal = float(input('Olá {}! Vamos calcular o seu aumento. Digite o seu salário atual:'.format(nome)))

# calculo 
if sal >= 1250:
    menordesc = (sal * 0.10) + sal
    print('{}, seu salário era de R${:.2f}, com um aumento de 10%, você passará a receber R${:.2f}!'.format(nome,sal,menordesc))
else: 
    maiordesc = (sal * 0.15) + sal
    print('{}, seu salário era de R${:.2f}, com o aumento de 15%, você passará a receber R${:.2f}!'.format(nome,sal,maiordesc))
print('Obrigada por trabalhar conosco!')


