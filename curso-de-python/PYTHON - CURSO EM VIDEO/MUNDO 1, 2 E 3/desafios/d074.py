# DESAFIO 074 - Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.

# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor da tupla.

from random import randint

conj = ()

for c in range (0,5):
    num = randint(0, 11)
    conj += num,  

print(f'Os valores sorteados foram {conj}')
print(f'O maior número sorteado foi {max(conj)}')
print(f'O menor número sorteado foi {min(conj)}')

#corrigido 






