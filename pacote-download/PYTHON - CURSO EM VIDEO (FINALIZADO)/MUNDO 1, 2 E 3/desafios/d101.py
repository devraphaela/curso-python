# DESAFIO 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.



def voto(nasc):
    from datetime import datetime

    i = datetime.now().year - nasc
    if i < 16:
        return f'Com {i} anos: NÃO VOTA!'
        
    elif i == 16 or i == 17 or i >= 65:
        return f'Com {i} anos: VOTO OPCIONAL!'
    else:
        return f'Com {i} anos: VOTO OBRIGATÓRIO!'
    
#programa principal
print('-'*30)    
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

#corrigido