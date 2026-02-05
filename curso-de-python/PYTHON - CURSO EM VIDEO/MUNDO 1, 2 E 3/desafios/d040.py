# DESAFIO 040 - Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final de acordo com a média atingida
# abaixo de 5 = REPROVADO
# entre 5 e 6.9 = RECUPERAÇÃO
# media 7 ou superior = APROVADO


nome_Aluno = str(input('Digite o nome completo do aluno: '))
nome = nome_Aluno.split()
n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
m = (n1 + n2) /2

if m < 5:
    print('Poxa {}, sua média foi {:.1f}. Infelizmente você está reprovado.'.format(nome[0],m))
elif m >= 5 and m <= 6.9:
    print('Estude mais {}, sua média foi {:.1f}. Infelizmente você está de recuperação.'.format(nome[0],m))
else:   
    print ('Parabéns {}! sua média foi {:.1f}. Você está aprovado.'.format(nome[0],m))

#corrigido