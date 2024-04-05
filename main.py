
import sys
import threading
from mapReduce import Mape, Reducee


def initMap(arqv, padrao, results, lock):
    resultMap = Mape(arqv, padrao)
    if resultMap:
        with lock:
            results.append(resultMap)

def initReduce(results, lock):
    if not results:
         return
    
    resultReduce = Reducee(results)
    for numLinha , linha in resultReduce:
        print(f"{numLinha}--- {linha} ")

def Grep(arqvs , padrao):
    resultsMaps = []
    threadsMap = []
    lock = threading.Lock()
    for arq in arqvs:
            thread = threading.Thread(target=initMap, args=(arq, padrao, resultsMaps, lock))
            threadsMap.append(thread)
            thread.start()
    for thread in threadsMap:
         thread.join()

    initReduce(resultsMaps, lock)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    padrao = sys.argv[1]
    arquivos = ["input0", "input1", "input2", "input3"]
    lock = threading.Lock()
    Grep(arquivos, padrao)