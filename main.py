import threading
from mapReduce import Map, Reduce


def initMap(arqv, padrao, results):
    resultMap = Map(arqv, padrao)
    results.append(resultMap)


def initReduce(results):
    resultReduce = Reduce(results)
    for numLinha , linha in resultReduce:
        print(f"{numLinha}--- {linha} ")

def Grep(arqvs , padrao):
    resultsMaps = []
    threadsMap = []
    for arq in arqvs:
            thread = threading.Thread(target=initMap, args=(arq, resultsMaps))
            threadsMap.append(thread)
            thread.start()
    for thread in threadsMap:
         thread.join()

    initReduce(resultsMaps)