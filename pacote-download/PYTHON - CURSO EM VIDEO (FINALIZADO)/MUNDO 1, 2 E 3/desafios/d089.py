# DESAFIO 089 -  Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a média de cada um e permita que o usuário possa ver as notas de casa aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media]) # lista composta

    perg = str(input('Quer continuar? [S/N]')).upper().strip()
    if perg != 'S':
        break

print('=-'*20)
print('BOLETIM ESCOLAR DA TURMA'.center(35))
print('=-'*20)
print('Nº', end='           ')
print('NOME', end='           ')
print('MÉDIA')
print('-'*40)

for c in enumerate(ficha):
    print(c[0], end='            ')
    print(c[1][0], end='             ')
    print(c[1][2])

while True:
    perg2 = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if perg2 <= len(ficha) -1:
        print(f'As notas de {ficha[perg2][0]} são {ficha[perg2][1]}')
    if perg2 == 999:
        break

print('Volte sempre')

#corrigido



