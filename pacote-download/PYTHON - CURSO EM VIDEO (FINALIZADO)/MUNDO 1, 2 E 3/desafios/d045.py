# DESAFIO 045 - Crie um programa que faça o computador jogar jokenpo com você.

# RESOLUÇÃO

from random import choice

nome = str(input('Olá! Digite o seu nome: ')).title().strip()
print(f'{nome}, vamos jogar jokenpô?')

# escolha do computador 
jokenpo = ['pedra','papel','tesoura']
escolha_Computador = choice(jokenpo)

# escolha do jogador
escolha_Jogador = str(input('Escolha: pedra, papel ou tesoura? ')).lower().strip()


if escolha_Jogador not in jokenpo:
    print(f'Escolha inválida {nome}, tente outra vez.')

else: 
    print(f'Você escolheu {escolha_Jogador} e o computador escolheu {escolha_Computador}.')

    # empate 
    if escolha_Computador == escolha_Jogador: 
        print(f'EMPATE! Tente outra vez {nome}.')

    # jogador ganha
    elif (escolha_Jogador == 'pedra' and escolha_Computador == 'tesoura' or escolha_Jogador == 'papel' and escolha_Computador == 'pedra' or escolha_Jogador == 'tesoura' and escolha_Computador == 'papel'):
        print(f'GANHOU! Parabéns {nome}.') 

    # jogador perde 
    else:
        print(f'PERDEU! Tente outra vez, {nome}.') 

print('É sempre muito legal jogar com você. Vamos de novo?')
