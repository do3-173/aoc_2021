from collections import deque
from copy import deepcopy

def uvecajMatricu(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            matrica[i][j] += 1

def dajFlash(matrica):
    rezultat = 0
    m = len(matrica)
    n = len(matrica[0])
    smjer = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    postaviFlash = set()
    dek = deque()
    for i in range(m):
        for j in range(n):
            if matrica[i][j] > 9:
                dek.append((i, j))
                postaviFlash.add((i, j))
    while dek:
        i, j = dek.popleft()
        rezultat += 1
        for di, dj in smjer:
            ni = di + i
            nj = dj + j
            if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in postaviFlash:
                continue
            matrica[ni][nj] += 1
            if matrica[ni][nj] > 9:
                postaviFlash.add((ni, nj))
                dek.append((ni, nj))
    for i, j in postaviFlash:
        matrica[i][j] = 0
    return rezultat


f = open("input/11.txt", "r")

nizLinija=f.readlines()
matrica=[]
for i in range(len(nizLinija)):
    niz=[]
    for j in range(len(nizLinija[i])-1):
        niz.append(int(nizLinija[i][j]))
    matrica.append(niz)

koraci=100
matrica1=deepcopy(matrica)
rezultat = 0
for i in range(koraci):
    uvecajMatricu(matrica1)
    rezultat += dajFlash(matrica1)

print(rezultat)

matrica2=deepcopy(matrica)
koraci = flashes = 0

while flashes != len(matrica2) * len(matrica2[0]):
    uvecajMatricu(matrica2)
    flashes = dajFlash(matrica2)
    koraci += 1
print(koraci)
