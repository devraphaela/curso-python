# DESAFIO 044 - Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# a vista dinheiro/cheque = 10% de desconto = a
# a vista cartão = 5% de desconto = b
# em até 2x no cartão = preço normal = c
# 3x ou mais no cartão = 20% juros = d


# RESOLUÇÃO

# programa que calcule o valor a ser pago por um produto
print('Bem vindo(a) a nossa loja!')
valor = float(input('Digite o valor do produto em R$: '))
pgto = str(input(' a. À vista - dinheiro \n b. À vista - cartão \n c. 2x no cartão \n d. 3x ou mais no cartão \n Digite o metodo de pagamento: ')).strip()

# considerando o seu preço normal e condição de pagamento:
a = valor - (valor * 0.10)
b = valor - (valor * 0.05)
c = valor 
d = valor + (valor * 0.20)


# condições
if pgto.lower() == 'a':
    print('Você escolheu o pagamento à vista - dinheiro! Desconto de 10% aplicado, o valor a pagar será de R${:.2f}'.format(a))

elif pgto.lower() == 'b':
    print('Você escolheu o pagamento à vista - cartão! Desconto de 5% aplicado, o valor a pagar será de R${:.2f}'.format(b))

elif pgto.lower() == 'c':
    print('Você escolheu o pagamento em até 2x no cartão! O valor a pagar será de R${:.2f}'.format(c))

elif pgto.lower() == 'd':
    print('Você escolheu o pagamento 3x ou mais no cartão! Taxa de 20% de jusros aplicada, o valor a pagar será de R${:.2f}'.format(d))

print('Obrigada por comprar conosco! Volte sempre.')




