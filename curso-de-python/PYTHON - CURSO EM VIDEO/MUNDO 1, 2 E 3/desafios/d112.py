# DESAFIO 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dados. Crie uma função chamado leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadesCev import moeda, dados

p = dados.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 80, 35, True)

#corrigido