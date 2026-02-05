# DESAFIO 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:

# quantas pessoas tem mais de 18 anos.
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos.

mais_18 = 0
homens = 0
mumenos_20 = 0

while True:
    print('Vamos coletar alguns dados! ')
    idade = int(input('Digite a sua idade [EX: 20]: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).lower().strip()
    
    if idade >= 18:
        mais_18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mumenos_20 += 1
        
    perg = str(input('Você quer continuar registrando? [S/N]')).lower().strip()
    if perg != 's':
        break

print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoa com mais de 18 anos: {mais_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'Temos {mumenos_20} mulheres com menos de 20 anos')

#corrigido
