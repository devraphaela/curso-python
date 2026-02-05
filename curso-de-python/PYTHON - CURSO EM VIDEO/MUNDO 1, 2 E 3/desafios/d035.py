# DESAFIO 035 - Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

# pesquisar princípio do triangulo

# a soma do angulo tem que ser 180 graus

print('Vamos ver se as suas retas formam ou não um triângulo!')
r1 = int(input('Digite o comprimento da primeira reta:'))
r2 = int(input('Digite o comprimento da segunda reta:'))
r3 = int(input('Digite o comprimento da terceira reta:'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Ótimo! com as retas {}, {} e {} é possível formar um triângulo.'.format(r1,r2,r3))
else:
    print('Infelizmente com as retas {}, {} e {} não é possível formar um triângulo!'.format(r1,r2,r3))