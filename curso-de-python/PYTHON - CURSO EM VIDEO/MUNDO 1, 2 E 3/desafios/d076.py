# DESAFIO 076 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência

# No final, mostre uma listagem de preços organizando os dados em forma tabular.

listagem = ('Agenda', 30.00 , 'Caderno', 25.00 , 'Caneta', 3.00, 'Lapiseira', 8.00, 'Borracha', 2.50, 'Canetinha', 17.99, 'Fichario', 59.90, 'Mochila', 105.79, 'Estojo', 27.90)

print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*30)

for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>3.2f}')

print('-'*30)

#corrigido