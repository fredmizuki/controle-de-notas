# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*vnotas, situacao=False):
    dic = {}
    dic['Total'] = len(vnotas)
    dic['Maior'] = max(vnotas)
    dic['Menor'] = min(vnotas)
    dic['Media'] = sum(vnotas) / len(vnotas)
    if situacao:
        if dic['Media'] >= 7:
            dic['Situação'] = 'Boa'
        elif dic['Media'] >= 5:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'
    return dic
