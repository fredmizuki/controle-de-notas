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
