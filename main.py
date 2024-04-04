import sys
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
            thread = threading.Thread(target=initMap, args=(arq, padrao, resultsMaps))
            threadsMap.append(thread)
            thread.start()
    for thread in threadsMap:
         thread.join()

    initReduce(resultsMaps)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    padrao = sys.argv[1]
    arquivos = ["input0"]
    Grep(arquivos, padrao)