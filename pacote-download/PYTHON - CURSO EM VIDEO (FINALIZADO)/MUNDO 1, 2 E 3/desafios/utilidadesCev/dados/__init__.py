def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'ERRO! {valor} é inválido. Digite um número válido.')
        else:
            valido = True
            return float(valor)
        

#corrigido