# VARIÁVEIS COMPOSTAS (LISTAS)

# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

# lanche.append('cookie') PARA ADICIONAR ELEMENTOS NO FINAL
# lanche.insert(0,'cachorro quente') PARA ADICIONAR ELEMENTOS EM POSIÇÃO ESPECÍFICA
# lanche.pop() PARA APAGAR O ÚLTIMO ELEMENTO DA LISTA 
# lanche.pop(3) PARA APAGAR ALGO DA LISTA PELO ÍNDICE
# lanche.remove('pizza') PARA APAGAR ALGO DA LISTA PELO CONTEÚDO

# if 'pizza' in lanche:
#     lanche.remove('pizza')


# valores = list(range(4,11))
# valores = [8,2,5,4,9,3,0]
# valores.sort()
# valores.sort(reverse=True)


# #PRÁTICA
# num = [2,5,9,1]
# num[2] = 3 # mudar
# num.append(7) # adicionar 
# num.sort() # ordenar
# num.sort(reverse=True) # reverso
# num.insert(2,0) # na posição 2, adicionar o 0
# num.pop() # remove o ultimo
# num.pop(2)  # remove um elemento escolhido
# if 4 in num:
#     num.remove(4)
# else:
#     print('não achei o numero 4')
# print(num)
# print(f'essa lista tem {len(num)} elementos')



# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))


# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')


a = [2,3,4,7]
b = a[:] # copia dos valores ((NAO CRIA UMA LIGAÇAO))
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')

