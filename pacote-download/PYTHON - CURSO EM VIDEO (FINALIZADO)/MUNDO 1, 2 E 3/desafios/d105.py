# DESAFIO 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as docstrings da função.



def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notFinal = dict()
    notFinal['total'] = len(num)
    notFinal['maior'] = max(num)
    notFinal['menor'] = min(num)
    notFinal['media'] = sum(num) / len(num)
    if sit:
        if notFinal['media'] > 7:
            notFinal['situação'] = 'BOA'
        elif notFinal['media'] >= 5:
            notFinal['situação'] = 'RAZOÁVEL'
        else:
            notFinal['situação'] = 'RUIM'
    return notFinal

  


# programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

#corrigido