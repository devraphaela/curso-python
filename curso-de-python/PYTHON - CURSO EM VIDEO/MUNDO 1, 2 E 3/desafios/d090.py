# DESAFIO 090 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo na tela.

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
    if aluno['media'] <= 4.9:
        print('Situação é igual a Reprovado.')
    else:
        print('Situação é igual a Aprovado.')

#corrigido