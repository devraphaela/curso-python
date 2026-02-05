# DESAFIO 108 - Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from utilidadesCev import moeda 

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')

#corrigido