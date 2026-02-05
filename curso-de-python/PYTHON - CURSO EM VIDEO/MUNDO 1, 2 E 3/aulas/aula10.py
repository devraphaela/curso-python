# CONDIÇÕES

# carro = objeto
# siga = método () sempre com parenteses no final 

# estrutura sequencial 
    # linha reta sem desvios 

# if = bloco verdadeiro 
# else = bloco falso


# carro.siga()
# se carro.esquerda(): dois pontos obrigatorios
    # carro.siga()
    # carro.direita()
    # carro.siga()
    # carro.direita()
    # carro.esquerda()
    # carro.siga()
    # carro.direita()
    # carro.siga()
# senão: (else)
    # carro.siga()
    # carro.esquerda()
    # carro.siga()
    # carro.esquerda()
    # carro.siga()
# carro.pare()


# PRÁTICA - Somente com if 
nome = str(input('Digite o seu nome:'))
if nome == 'Gustavo':
    print('Que nome lindo vc tem {}!'.format(nome))
print('Bom dia {}!'.format(nome))


# PRÁTICA - Com if e else
nome2 = str(input('Digite o seu nome:'))
if nome2 == 'Gustavo':
    print('Bom dia {}! Eu adoro o seu nome.'.format(nome2))
else:
    print('Não gosto do seu nome, deveria ser Gustavo!')
print('Bom dia mesmo assim {}.'.format(nome2))


# PRÁTICA - MEDIA ALUNO
nome = str(input('Digite o seu nome:'))
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
m = (n1+ n2) /2

if m >= 6:
    print('Parabéns {}! Continue assim.'.format(nome))
else:
    print('Poxa {}!, você precisa melhorar...'.format(nome))
print('A sua média foi {:.1f}'.format(m))