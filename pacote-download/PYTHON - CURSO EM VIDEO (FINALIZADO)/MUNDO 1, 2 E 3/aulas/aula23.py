# TRATAMENTO DE ERROS E EXCEÇÕES

# erros de sintaxe são erros digitados

# exceção são os erros de "lógica"

#try:
    #se eu tentar esse comando e não funcionar
#except:
    # o que vai acontecer 

# except Exception as erro:
#     print('Infelizmente tivemos um problema...')
#     print(f'O que aconteceu foi {erro.__class__}')


try:
    a = int(input('primeiro num: '))
    b = int(input('segundo num: '))
    r = a / b
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre!')