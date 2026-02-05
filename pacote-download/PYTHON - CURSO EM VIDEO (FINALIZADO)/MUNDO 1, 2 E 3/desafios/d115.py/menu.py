# DESAFIO 115a - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def leiaInt(msg):
    while True:
        try:
            valorInt = int(input(msg))
        except(ValueError, TypeError):
            print('Erro! Digite um número válido')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar o valor.')
            return 0
        else:
            return valorInt

def menu(lista):
    cadastro = list()
    while True:
        print('-'*30)
        print('MENU PRINCIPAL'.center(30))
        print('-'*30)
        c = 1
        for c, item in enumerate(lista, start=1):
            print(f'{c} - {item}')
        print('-'*30)

    
        opc = leiaInt('Sua opção: ')

        if opc == 1:
            print('-' * 30)
            print('PESSOAS CADASTRADAS'.center(30))
            print('-' * 30)
            if not cadastro:
                print('Nenhuma pessoa cadastrada.')
            else:
                for p in cadastro:
                    print(f'{p[0]} \t {p[1]} anos')
            

        elif opc == 2:
            print('-'*30)
            print('NOVO CADASTRO'.center(30))
            print('-'*30)
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            cadastro.append([nome, idade])
            print('Cadastro efetuado com sucesso!')
    
        elif opc == 3:
            print('Saindo do sistema... Até logo!')
            break
        else:
            print('Responda apenas com 1, 2 ou 3.')

        



