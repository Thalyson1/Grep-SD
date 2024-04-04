import threading
from mapReduce import Map, Reduce


def initMap(arqv, padrao, results):
    resultMap = Map(arqv, padrao)
    results.append(resultMap)


