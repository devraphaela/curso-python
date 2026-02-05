# while True
    # if chao:
        #passo
    #if buraco:
        #pula
    #if moeda:
        #pega
    #if trofeu:
        #pula
        #break joga pra fora do laço
#pega

n = 0
s = 0

while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += 1
print(f'A soma vale {s}')
