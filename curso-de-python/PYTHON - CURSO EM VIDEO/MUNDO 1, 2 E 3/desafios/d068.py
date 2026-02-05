# DESAFIO 068 - Faça um programa que joque par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*20)

vit = 0

while True:
    num_Jog = int(input('Diga um valor: [DE 1 A 10]: '))
    esc_Jog = str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).lower().strip()[0]


    num_Pc = randint(0, 10)
    soma = num_Jog + num_Pc

    print(f'Você escolheu o número {num_Jog}, o computador escolher o numero {num_Pc}')

    if soma % 2 == 0:
        resultado = 'p'
        print('DEU PAR')
        
    else:
        resultado = 'i'
        print('DEU ÍMPAR')

    if resultado == esc_Jog:
        print('Você venceu!!')
        vit += 1
    else:
        print('Você perdeu!')
        break
print(f'GAME OVER! Você conseguir {vit} vitórias consecutivas.')

#corrigido




    




