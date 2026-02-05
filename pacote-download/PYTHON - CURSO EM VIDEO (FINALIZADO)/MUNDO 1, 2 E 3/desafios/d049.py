# DESAFIO 049 - Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora usando o laço for.

num = int(input('Digite um número para saber a tabuada: '))

for c in range (0, 11):
    print(f'{num} x {c} = {num*c}')

#CORRIGIDO