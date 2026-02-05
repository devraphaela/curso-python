# DESAFIO 043 - Crie um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5 = ABAIXO DO PESO 
# entre 18.5 e 25 = PESO IDEAL 
# acima de 25 até 30 = SOBREPESO
# acima de 30 até 40 = OBESIDADE
# acima de 40 = OBESIDADE MÓRBIDA

# RESOLUÇÃO

# programa que leia o peso e a altura de uma pessoa
nome = str(input('Digite o seu nome: '))
peso = float(input('Digite o seu peso (Ex: 60.0): '))
altura = float(input('Digite a sua altura: (Ex: 1.80): '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('ABAIXO DO PESO! {}, seu IMC é {:.1f}, procure um médico pois você pode estar com desnutrição.'.format(nome,imc))
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL! {}, seu IMC é {:.1f}, você está saudável.'.format(nome,imc))
elif imc <= 30:
    print('SOBREPESO! {}, seu IMC é {:.1f}, procure um médico pois você pode estar com problemas de saúde.'.format(nome,imc))
elif imc <= 40:
    print('OBESIDADE! {}, seu IMC é {:.1f}, procure assim que possível um médico pois você pode estar com problemas de saúde.'.format(nome,imc))
else:
    print('OBESIDADE MÓRBIDA! {}, seu IMC é {:.1f}, procure urgente um médico pois você pode estar correndo sérios riscos de saúde.'.format(nome,imc))

#corrigido