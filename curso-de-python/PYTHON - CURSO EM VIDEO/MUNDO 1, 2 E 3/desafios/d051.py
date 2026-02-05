# DESAFIO 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('10 TERMOS DE UMA PA')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range (primeiro, decimo + razao, razao):
    print(c)
    
print('Acabou')

#CORRIGIDO