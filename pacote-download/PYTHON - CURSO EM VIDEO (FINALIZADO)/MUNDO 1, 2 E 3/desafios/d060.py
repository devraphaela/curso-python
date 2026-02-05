# DESAFIO 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.

# ex: 5! = 5x4x3x2x1 = 120


num = int(input('Digite um número para saber o seu fatorial: '))
fatorial = 1
contador = num



while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'O fatorial de {num} é {fatorial}')


#corrigido
