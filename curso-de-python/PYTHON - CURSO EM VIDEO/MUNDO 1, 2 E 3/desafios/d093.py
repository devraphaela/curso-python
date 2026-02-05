# DESAFIO 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos e cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
tot = 0

jogador['nome'] = str(input('Nome do jogador: '))
perg = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# gols
for c in range(perg):
    gols.append(int(input(f'Quantos gols na partida {c}: '))) 
jogador['gols'] = gols

# total
for c in gols:
    tot += c
jogador['total'] = tot

# resultados 
print('=-'*35)
print(jogador)
print('=-'*35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*35)
print(f'O jogador {jogador["nome"]} jogou {perg} partidas.')
for i, g in enumerate(gols):
    print(f'=> Na partida {i}, fez {g} gols.'.center(35))
print(f'Foi um total de {jogador["total"]} gols.')


#corrigido