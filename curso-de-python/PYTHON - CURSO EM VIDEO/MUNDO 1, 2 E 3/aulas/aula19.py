# VARIÁVEIS COMPOSTAS (DICIONÁRIOS) { }

# dados = dict()
# dados = {}


# dados = {'nome': 'Pedro', 'idade': 25}
# print(dados['nome']) Pedro
# print(dados['idade']) 25

# dados['sexo'] = 'M' // PARA ADICIONAR NO DICIONÁRIO
# del dados['idade'] // PARA DELETAR ALGO NO DICIONÁRIO




# filme = {'título': 'Star Wars', 
#          'ano': 1977, 
#          'diretor': 'George Lucas'
# }

# print(filme.values()) # PRINTA TODOS OS VALORES (['Star Wars', 1977, 'George Lucas'])

# print(filme.keys()) # PRINTA TODAS AS CHAVES (['título', 'ano', 'diretor'])

# print(filme.items()) #PRINTA TODOS OS ITENS ([('título', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# for k, v in filme.items():
#     print(f'O {k} é {v}')

#PRÁTICA

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
# for k in pessoas.keys():
#     print(k)


# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])


estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # copiar 
for e in brasil:
    for v in e.values():
        print(v)




