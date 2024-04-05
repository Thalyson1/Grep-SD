import re

def Mape(arquivo, conteudo):
    linhasBatidas= []
    with open(arquivo, 'r') as arqv:
        for numLinha, linha in enumerate(arqv, start=1):
            if re.search(conteudo, linha):
                linhasBatidas.append((numLinha, linha.strip()))
    return linhasBatidas



def Reducee(results):
    if not results:
        return []

    resultadoFinal = []
    for resultado in sorted(results, key=lambda x: x[0]):
        for num_linha, linha in resultado:
            resultadoFinal.append((num_linha, linha))
    return resultadoFinal