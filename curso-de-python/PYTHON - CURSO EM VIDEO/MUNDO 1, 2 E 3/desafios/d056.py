# DESAFIO 056 - Crie um programa que leia o nome, idade e sexo de 4 pessoas e mostre:
# a média de idade do grupo
# o nome do homem mais velho
# quantas mulheres tem menos de 21 anos

#media
soma_idade = 0
media_idade = 0

#homem mais velho
maior_idade_homem = 0
nome_mais_velho = 0

# quantas mulheres tem menos de 21 anos
total_mulher_20 = 0

for c in range (0,4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o seu sexo (Ex: Masculino/Feminino): '))
    if c == 1 and sexo in 'Masculinomasculino':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Masculinomasculino' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Femininofeminino' and idade <20:
        total_mulher_20 += 1 

media_idade = soma_idade / 4
print(f'A media de idade do grupo é de {media_idade} anos.')
print(f'O home mais velho tem {maior_idade_homem} e seu nome é {nome_mais_velho}.')
print(f'Ao todo tem {total_mulher_20} mulheres com menos de 20 anos.')

#CORRIGIDO