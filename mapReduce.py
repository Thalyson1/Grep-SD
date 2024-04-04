import re

def Map(arquivo, conteudo):
    linhasBatidas= []
    with open(arquivo, 'r') as arqv:
        for numLinha, linha in enumerate(arqv, start=1):
            if re.search(conteudo, linha):
                linhasBatidas.append((numLinha, linha.strip()))
    return linhasBatidas
