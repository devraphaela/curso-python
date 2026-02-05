# DESAFIO 092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição).

from datetime import date
ano_atual = date.today().year

ficha = {}


ficha['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ficha['idade'] = ano_atual - nasc
ficha['ctps'] = int(input('Carteira de Trabalho (Digite 0 se não tiver): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['salário'] = float(input('Salário: R$'))
    idade_Contr = ficha['contratação'] - nasc
    ficha['aposentadoria'] = idade_Contr + 35

print('=-'*35)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')

#corrigido
