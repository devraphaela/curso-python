# MÓDULOS E PACOTES 

# MODULARIZAÇÃO (arquivo .py)

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')


# VANTAGENS DA MODULARIZAÇÃO
# organização
# facilita manutenção
# ocultação do codigo detalhado
# reutilizar em outros projetos




# PACOTE (pasta com um arquivo __init__.py dentro)
# uma pasta que contém módulos por 'assuntos'

# + UTEIS           # pasta (pacote)
    # - cores       # módulos por tema
        # - __init__.py            # arquivo criado em cada módulo
    # - datas       # módulos por tema
        # - __init__.py            # arquivo criado em cada módulo
    # - numeros     # módulos por tema
        # - __init__.py            # arquivo criado em cada módulo
    # - strings     # módulos por tema
        # - __init__.py            # arquivo criado em cada módulo
