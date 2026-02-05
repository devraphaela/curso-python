# DESAFIO 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# EX: 
# APOS A SOPA 
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO 
# ANOTARAM A DATA DA MARATONA

frase = (input('Digite a sua frase para saber se ela é um palíndromo: ')).strip().upper().replace(' ', '')
invertida = '' # string vazia


for c in frase:
    invertida = c + invertida 

print(f'Frase original: {frase}')   
print(f'Frase invertida: {invertida}')

if frase == invertida:
    print('elas são exatamente iguais, portanto é um palíndromo')
else:
    print('elas não são exatamente iguais, portanto não é um palíndromo.')

#CORRIGIDO
    

