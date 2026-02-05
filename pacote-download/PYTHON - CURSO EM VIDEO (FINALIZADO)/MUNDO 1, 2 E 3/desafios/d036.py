# DESAFIO 036 - Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado




# RESOLUÇÃO

# Programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
print('Olá somos do setor de financiamentos da Caixa!')
nome = str(input('Digite o seu nome completo: '))
prim_nome = nome.split()
renda = float(input('{}, qual a sua renda mensal em R$? '.format(prim_nome[0])))
valor_Casa = float(input('{}, qual o valor em R$ do imóvel desejado? '.format(prim_nome[0])))
anos = int(input('{}, em quantos anos você pretende pagar este imóvel? '.format(prim_nome[0])))
meses = anos * 12

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado
parcela = valor_Casa / meses

# Condição do financiamento 
if parcela > renda * 0.30:
    print('FINANCIAMENTO NEGADO! {}, entendo que esteja querendo comprar este imóvel agora, mas sua renda está muito baixa no momento para uma parcela de R${:.2f}. Tente outro imóvel ou guarde mais dinheiro.'.format(prim_nome[0],parcela))
elif parcela == renda * 0.30:
    print('FINANCIAMENTO PARCIALMENTE APROVADO! {}, Seu emprestimo foi aprovado, porém de acordo com o cálculo sua parcela mensal ficará em R${:.2f} e isso pode ficar apertado no seu bolso. Se programe antes de assinar o financiamento.'.format(prim_nome[0],parcela))

else:
    print('FINANCIAMENTO APROVADO! Parabéns {}, você está apto(a) para adiquirir este imóvel, sua parcela mensal ficará em R${:.2f}.'.format(prim_nome[0],parcela))


# corrigido 

