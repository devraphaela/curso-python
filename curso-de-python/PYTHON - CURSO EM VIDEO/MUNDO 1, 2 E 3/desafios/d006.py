#DESAFIO 006 - Crie um algorítmo que leia um número e mostre o seu dobro, tríplo e raiz quadrada.

num = int(input('Digite um número:'))
dobro = int(num * 2)
triplo = int(num * 3)
raiz = int(num **(1/2))

print('O número que você escolheu foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(num,dobro,triplo,raiz))


 #CORRIGIDO