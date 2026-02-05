# LAÇO DE REPETIÇÃO WHILE 

# Estrutura de repetição com teste lógico (enquanto)

# while not maça:
#     passo
# pega maça

# while not maça:
#   if chão:
#     passo
#   if buraco:
#     pula
#   if moeda:
#     pega
# pega maça

# PRATICA

# c = 1
# while c < 10:
#     print(c)
#     c += 1

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? S/N: ')).upper()

# print('FIM')

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares, e {impar} números ímpares.')