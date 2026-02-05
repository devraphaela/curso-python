# FUNÇÕES PT1

# def mostraLinha():
#     print('-'*30)     # declarar a função

# mostraLinha()   # chamar a função (mostrar na tela)
# print('oi')
# mostraLinha()



# FUNÇÕES COM PARÂMETROS

# print('-'*30)
# print('SISTEMA DE ALUNOS')
# print('-'*30)

# print('-'*30)
# print('CADASTRO DE FUNCIONARIOS')
# print('-'*30)

# print('-'*30)
# print('ERRO DO SISTEMA')
# print('-'*30)


# def mensagem(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)

# mensagem('SISTEMA DE ALUNOS')



# declaração de função
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


# programa principal
titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')



#PRÁTICA

# declaração de função
def soma (a, b):
    s = a + b
    print(s)

# programa principal
soma(4, 5) # não declarar nenhum
soma(b=8, a=9) # ou declarar OS DOIS
soma(2, 1)



# EMPACOTAR PARÂMETROS
def contador(*num): # sem declarar quantidade de parâmetros
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')

contador(5, 7, 3, 1, 4) 
contador(8, 4, 7)
# tupla criada

# DESEMPACOTAR 
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')



#USANDO LISTA
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]

# programa principal
dobra(valores)
print(valores)
