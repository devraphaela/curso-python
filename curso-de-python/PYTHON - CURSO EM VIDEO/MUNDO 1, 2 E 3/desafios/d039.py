# DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo do alistamento

# de acordo com ano atual calculo

# o programa deverá mostrar também o tempo que falta ou quanto passou do prazo


# RESOLUÇÃO 

# programa que leia o ano de nascimento de um jovem
print('Bem vindo ao serviço militar!')
nome = str(input('Digite o seu nome: '))
nasc = int(input('Digite seu ano de nascimento: '))
ano = int(input('Digite o ano atual: '))

# calculo da idade 
idade = ano - nasc

# calculo falta 
menos = 18 - idade
mais = idade - 18 


# condiçoes
if idade < 17:
    print('{}, você está com {} anos, então ainda não precisa se alistar, somente daqui a {} anos.'.format(nome,idade,menos))
elif idade == 17:
    print('{}, você está com {} anos, então ainda não precisa se alistar, somente daqui a {} ano.'.format(nome,idade,menos))
elif idade == 18:
    print('{}, você está com {} anos! Esta é a idade exata para se alistar, por favor preencha seu cadastro.'.format(nome,idade))
elif idade == 19:
    print('{}, você está com {} anos, você está {} ano atrasado para o alistamento, entre em contato com o SAC.'.format(nome,idade,mais))
elif idade > 19:
    print('{} você está com {} anos, você está {} anos atrasado para o alistamento, entre em contato com o SAC.'.format(nome,idade,mais))

#corrigido