# DESAFIO 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.




while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    if num < 0:
        break

    print('-' *30)
    for c in range (0,11):
        print(f'{num} x {c} = {num*c}')
    print('-' *30)   
    
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

#corrigido