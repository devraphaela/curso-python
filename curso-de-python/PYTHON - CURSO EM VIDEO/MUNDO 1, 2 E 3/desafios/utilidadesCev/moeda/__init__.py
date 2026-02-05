def moeda(n = 0, m= 'R$'):
    return f'{m}{n}'.replace('.', ',')


def aumentar(n=0, p=0, m=True):
    valor = n + (n * p / 100)
    return valor if m == False else moeda(valor)
    

def diminuir(n=0, p=0, m=True):
    valor = n - (n * p / 100)
    return valor if m == False else moeda(valor)   


def dobro(n=0, m=True):
    valor = n * 2
    return valor if m == False else moeda(valor)


def metade(n=0, m=True):
    valor = n / 2
    return valor if m == False else moeda(valor) 


def resumo(n=0, a=10, r=5, m=True):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)

    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{r}% de redução: \t{diminuir(n, r)}')
    print('-'*30)