# DESAFIO 095 - Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de casa jogador.



jogadores = list()

while True:
    jogador = dict()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    perg = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    # gols
    gols = []
    for c in range(perg):
        gols.append(int(input(f'Quantos gols na partida {c+1}: '))) 
    jogador['gols'] = gols

    # total
    tot = 0
    for c in gols:
        tot += c
    jogador['total'] = tot

    # jogar para lista
    jogadores.append(jogador.copy())

    while True:
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()
        if perg in 'SN':
            break
        print('Responda apenas S ou N.')
    if perg != 'S':
        break

# resultados 
print('=-'*35)
print('COD', end='       ')
print('NOME', end='       ')
print('GOLS', end='       ')
print('TOTAL')

for i, j in enumerate(jogadores):
    print(f'{i:<9}{j["nome"]:<11}{str(j["gols"]):<11}{j["total"]}')

print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}: ')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('VOLTE SEMPRE')

#corrigido


