# CADEIA DE TEXTO 
# INDICE DE 0 A INFINITO



# VARIÁVEL 1
frase = 'Curso em vídeo Python'

#FATIAMENTO = pegar uma letra 
print(frase[9])

#FATIAMENTO = pegar um pedaço de algo (exclui o ultimo índice)
print(frase[9:13]) # inclui 9 e remove o 13

#FATIAMENTO = pegar uma parte do texto pulando de 2 em 2
print(frase[9:21:2])

#FATIAMENTO = começar do índice 0 até 5 (até o 4)
print(frase[:5])

#FATIAMENTO = começar do índice 15 até o final 
print(frase[15:])


#FATIAMENTO = começar do 9 e ir pulando de 3 em 3
print(frase[9::3])

#ANÁLISE 
print(len(frase)) # tamanho da frase = quantos indices 
print(frase.count('o')) # contar quantas vezes aparece a letra "o" 
print(frase.count('o',0,13)) # contar quantas vezes aparece a letra "o" do 0 ao 12
print(frase.find('deo')) # em qual índice começou o "deo"
print(frase.find('android')) # -1 quando não existir 
print(frase.rfind('a')) # a ultima vez que aparece a letra a
print('Curso' in frase) # se existe "Curso" na var frase (respeitando letra maiusc)

#TRANSFORMAÇÃO
print(frase.replace('Python','Android')) # vai substituir Python por Android
print(frase.upper()) # deixa toda a variável em letra maiusc
print(frase.lower()) # deixa toda a variável em letra minusc
print(frase.capitalize()) # deixa toda a var em minusc e deixa a primeira letra maiusc
print(frase.title()) # todo começo de palavra ele vai deixar em letra maiusc
 



# VARIÁVEL 2
frase2 = '   Aprenda Python  '

#TRANSFORMAÇÃO
print(frase2.strip()) # remove todos os espaços inúteis no começo e no fim da frase
print(frase2.rstrip()) # remove os espaços da direita
print(frase2.lstrip()) # remove os espaços da esquerda
print(frase2.split()) # gera uma lista separando todas as palavras dessa frase 
print('-'.join(frase2)) # juntar tudo separado por um - 
print(frase2.replace(' ', ''))