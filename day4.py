import numpy as np
import copy

def GetMatrix(matrica):
    nizBrojeva = []
    for red in matrica:
        noviNiz=[int(x) for x in red.strip().split()]
        nizBrojeva.append(noviNiz)
    return nizBrojeva

def OdigrajBingo(Tiket2,nizBrojeva):
    Tiket=copy.deepcopy(Tiket2)
    for i in range(5):
        for j in range(5):
            if Tiket[i][j] in nizBrojeva:
                Tiket[i][j]=1
            else:
                Tiket[i][j]=0
    Tiket=np.array(Tiket)
    suma_redova=np.sum(Tiket,axis=0)
    suma_kolona=np.sum(Tiket,axis=1)
    if 5 in suma_kolona or 5 in suma_redova:
        return True
    return False

def SaberiBingo(Tikets,nizBrojeva):
    Tiket = copy.deepcopy(Tikets)
    for i in range(5):
        for j in range(5):
            if Tiket[i][j] in nizBrojeva:
                Tiket[i][j]=0
    Tiket=np.array(Tiket)
    return np.sum(Tiket)

f = open("input/4.txt", "r")

nizLinija=f.readlines()
nizBrojevaString=nizLinija[0]
nizBrojeva=[int(x) for x in nizBrojevaString.split(',')]
i=2
nizTiketa=[]
while i<len(nizLinija):
    matrica=nizLinija[i:i+5]
    i+=6
    nizTiketa.append(GetMatrix(matrica))

suma=[]
for i in range(len(nizBrojeva)+1):
    nizTiketaPobjednickih = []
    for Tiket in nizTiketa:
        winning=OdigrajBingo(Tiket,nizBrojeva[0:i])
        if winning:
            suma.append(nizBrojeva[i - 1] * SaberiBingo(Tiket, nizBrojeva[0:i]))
            nizTiketaPobjednickih.append(Tiket)
    for pobjednickiTiket in nizTiketaPobjednickih:
        nizTiketa.remove(pobjednickiTiket)

print(suma[0])
print(suma[len(suma)-1])