# DESAFIO 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite


# programa que leia a velocidade de um carro.
nome = str(input('Digite o seu nome:'))
print('Olá {}! Nós somos da MULTA SIM OU NÃO, e vamos checar se você levou alguma multa.'.format(nome))
vel = float(input('Por favor, informe a velocidade (em km) em que você estava dirigindo:'))



if vel <= 80:
    print('{}, você estava dirigindo dentro do limite permitido. Você não foi multado(a)!'.format(nome))
else:
    ex = vel - 80
    multa = ex * 7
    print('{}, você foi multado(a)! Estava {} km acima da velocidade, portanto irá pagar R${:.2f} de multa.'.format(nome,ex,multa))

# corrigido 