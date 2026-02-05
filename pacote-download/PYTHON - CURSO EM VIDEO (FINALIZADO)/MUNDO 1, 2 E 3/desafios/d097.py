# DESAFIO 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mosrtre uma mensagem com tamanho adaptável.

# ex: escreva('Olá, Mundo!')
# saida: -----------
#        Olá, Mundo!
#        -----------

def escreva(txt):
    linha = len(txt) + 4
    print('-' * linha)
    print(f'  {txt}')
    print('-' * linha)

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

#corrigido