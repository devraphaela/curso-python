# DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez



# RESOLUÇÃO

# Leia uma frase 
frase = str(input('Digite uma frase:')).upper().split()

# Quantas vezes aparece a letra "a"
print('A letra A aparece {} vezes.'.format(frase.count('A')))

# Em que posição ela aparece a primeira vez
print('A primeira vez que a letra A aparece é no índice {}:'.format(frase.find('A')))

# Em que posição ela aparece a última vez
print('A última vez que a letra A aparece é no índice {}:'.format(frase.rfind('A')))

# CORRIGIDO
