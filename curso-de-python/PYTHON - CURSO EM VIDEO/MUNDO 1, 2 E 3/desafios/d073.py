# DESAFIO 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

# Apenas os 5 primeiros colocados
# Os últimos colocados
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time da Chapecoense

tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Internacional', 'Santos', 'Sport', 'Chapecoense', 'Fortaleza', 'Juventude', 'Ceará', 'Bragantino', 'Vitória', 'Atlético')

print('='*30)
print('CAMPEONATO BRASILEIRO DE FUTEBOL'.center(30))
print('='*30)

# Apenas os 5 primeiros colocados
print('Os 5 primeiros colocados do campeonato são:')
print('1º', tabela[0])
print('2º', tabela[1])
print('3º', tabela[2])
print('4º', tabela[3])
print('5º', tabela[4])

print('='*30)

# Os últimos colocados
print('Os 5 últimos colocados do campeonato são:')
print('16º', tabela[-5])
print('17º', tabela[-4])
print('18º', tabela[-3])
print('19º', tabela[-2])
print('20º', tabela[-1])

print('='*30)

# Um alista com os times em ordem alfabética
print(sorted(tabela))

print('='*30)


# Em que posição na tabela está o time da Chapecoense

print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}º posição')

print('='*30)
print('FIM')

#corrigido