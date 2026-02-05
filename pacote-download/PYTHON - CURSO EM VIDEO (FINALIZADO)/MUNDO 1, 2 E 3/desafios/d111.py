# DESAFIO 111 - Crie um pacote chamado utilidadeCeV que tenha dois módulos internos chamados moeda e dados.

# transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


from utilidadesCev import moeda

p = float(input('Digite um preço: R$'))
moeda.resumo(p, 80, 35, True)

#corrigido