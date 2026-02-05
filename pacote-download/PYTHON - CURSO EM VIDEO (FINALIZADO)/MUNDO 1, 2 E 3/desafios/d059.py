# DESAFIO 059 - Crie um programa que leia dois valores e mostre um menu na tela 
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.



# leia dois valores
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0

# menu de escolhas
while menu != 5:
    print('O que você quer fazer com esses 2 valores informados: ')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] O MAIOR NÚMERO')
    print('[4] DIGITAR NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')

    menu = int(input('Digite a opção escolhida: '))


    # opção escolhida
    print(f'Voce escolheu a opção {menu}')

    # soma
    if menu == 1:
        soma = num1 + num2
        print(f'A soma dos valores {num1} e {num2} é de {soma}')


    # multiplicação
    elif menu == 2:
        multi = num1 * num2
        print(f'A multiplicação dos valores {num1} e {num2} é de {multi}')

    # maior num
    elif menu == 3:
        maior = num1
        if num2 > maior:
            maior = num2
            print(f'E o maior número entre {num1} e {num2} é {maior}')
        if num1 == num2:
            print(f'Não existe um número maior entre {num1} e {num2}, os dois são iguais.')


    # digitar novos números
    elif menu == 4:
        print('Digite novos números.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    
    
    # sair do programa 
    elif menu == 5:
        print('Até mais!')
    #só sair se digitar 5
        
    else:
        print('Opção inválida, tente novamente.')

# CORRIGIDO