# FUNÇÕES PT2

# *** TÓPICOS DA AULA ***
# interactive help
# docstrings
# argumentos/parâmetros opcionais
# escopo de variaveis
# retorno de resultados/valores



# *** INTERACTIVE HELP ***
# help(print) # para mostrar a ajuda interativa
# print(input.__doc__) # para imprimir a docstring



# *** DOCSTRINGS ***
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Gustavo Guanabara do canal CursoemVideo.
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('FIM')

# contador(2, 10, 2)
#help(contador)



# *** ARGUMENTOS/PARÂMETROS OPCIONAIS ***
# def somar(a=0, b=0, c=0):   # se por acaso não tiver um parâmetro ele recebe 0 
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     Função criada por Gustavo Guanabara do canal CursoemVideo.
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(b=8, c=4)
# somar()



# *** ESCOPO DE VARIÁVEIS ***
#exemplo1
# def teste():
#     x = 8 # variável x tem um escopo LOCAL
#     print(f'Na função teste n vale {n}')
#     print(f'Na função teste, x vale {x}')

# #programa principal
# n = 2 # variável n tem um escopo GLOBAL
# print(f'No programa principal, n vale {n}')
# teste()
# print
# print(f'No programa principal, x vale {x}')


#exemplo2
# def funcao():
#     n1 = 4
#     print(f'n1 local vale {n1}')

# n1 = 2
# funcao()
# print(f'n1 global vale {n1}')


#exemplo3
# def teste(b):
#     global a # para usar variaveis globais dentro das funções
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')

# a = 5
# teste(a)
# print(f'A fora vale {a}')



# *** RETORNO DE VALORES/RESULTADOS ***
# RETURN
# def somar(a=0, b=0, c=0):   # se por acaso não tiver um parâmetro ele recebe 0 
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     Função criada por Gustavo Guanabara do canal CursoemVideo.
#     """
#     s = a + b + c
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)

# print(f'Meus calculos deram {r1}, {r2} e {r3}.')



#PRATICA
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados sao {f1}, {f2} e {f3}')

# ou
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')


#par ou impar
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input('Digite um número: '))
# if par(num):
#     print('é par!')
# else:
#     print('é ímpar!')