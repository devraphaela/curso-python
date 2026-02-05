# CONDIÇÕES ANINHADAS 
    # Estruturas condicionais dentro de outras estruturas condicionais 

# carro.siga()
# se carro.esquerda()
    #
    #   
    #
    #
# senao se carro.direita()
    #
    #   
    #
    #
# senao
    #
    #   
    #
    #
# carro.pare()


# PRATICA

nome = str(input('Digite o seu nome: '))

print('Bom dia {}!'.format(nome))
if nome == 'Gustavo':
    print('Que nome lindo.')
elif nome == 'Pedro' or nome == 'Maria':
    print('Que nome legal.')
else: 
    print('Eu não gosto do seu nome.')