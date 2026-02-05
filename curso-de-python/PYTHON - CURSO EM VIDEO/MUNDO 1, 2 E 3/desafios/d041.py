# DESAFIO 041 - Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# até 9 anos = MIRIM 
# até 14 anos = INFANTIL
# até 19 anos = JUNIOR
# até 25 anos = SENIOR
# acima = MASTER


# RESOLUÇÃO

# programa que leia o ano de nascimento de um atleta
nome_Atleta = str(input('Digite o seu nome: '))
ano_Nasc = int(input('Digite seu ano de nascimento: '))
ano_Atual = 2025
idade = ano_Atual - ano_Nasc

if idade <= 9:
    print('Atleta: {} \nCategoria: Mirim'.format(nome_Atleta))
elif idade <= 14:
    print('Atleta: {} \nCategoria: Infantil'.format(nome_Atleta))
elif idade <= 19:
    print('Atleta: {} \nCategoria: Junior'.format(nome_Atleta))
elif idade <= 25:
    print('Atleta: {} \nCategoria: Senior'.format(nome_Atleta))
else:
    print('Atleta: {} \nCategoria: Master'.format(nome_Atleta))

#corrigido


