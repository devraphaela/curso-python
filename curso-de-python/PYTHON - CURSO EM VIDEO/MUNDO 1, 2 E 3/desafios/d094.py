# DESAFIO 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:

# Quantas pessoas foram cadastradas.
# A média de idade do grupo.
# Uma lista com todas as mulheres.
# uma lista com todas as pessoas com idade acima da média. 

pessoas = list()
tot_Pessoas = 0
soma_Idade = 0
mulheres = list()

while True:
    cadastro = dict()
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite somente M ou F.')
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'].copy())
    cadastro['idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    tot_Pessoas += 1
    soma_Idade += cadastro['idade']
    while True:
        perg = str(input('Quer continuar? [S/N]')).upper().strip()
        if perg in 'SN':
            break
        print('ERRO! Responda somente S ou N.')
    if perg != 'S':
        break

media_Idade = soma_Idade / tot_Pessoas
print('=-'*35)
print(f'- O grupo tem {tot_Pessoas} pessoas.')
print(f'A média de idade é de {media_Idade:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print('Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media_Idade:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

#corrigido