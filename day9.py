f = open("input/9.txt", "r")

nizLinija = f.readlines()
matrica = []
for i in range(len(nizLinija)):
    niz = []
    for j in range(len(nizLinija[i]) - 1):
        niz.append(int(nizLinija[i][j]))
    matrica.append(niz)


def Vrijednost(matrica, tacka):
    if (tacka[0] < 0) or (tacka[0] >= len(matrica) - 1):
        return 10
    if (tacka[1] < 0) or (tacka[1] >= len(matrica[0]) - 1):
        return 10
    return matrica[tacka[0]][tacka[1]]

def prvi_dio():
    suma=0

    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            broj=matrica[i][j]
            if i-1<0 and j-1<0:
                if matrica[i+1][j]>broj and matrica[i][j+1]>broj:
                    suma+=(broj+1)
            elif i+1>=len(matrica) and j-1<0:
                if matrica[i-1][j]>broj and matrica[i][j+1]>broj:
                    suma+=(broj+1)
            elif i+1>=len(matrica)-1 and j+1>=len(matrica[i]):
                if matrica[i-1][j]>broj and matrica[i][j-1]>broj:
                    suma+=(broj+1)
            elif i-1<0 and j+1>=len(matrica[i]):
                if matrica[i+1][j]>broj and matrica[i][j-1]>broj:
                    suma+=(broj+1)
            elif i+1>=len(matrica):
                if matrica[i-1][j]>broj and matrica[i][j+1]>broj and matrica[i][j-1]>broj:
                    suma+=(broj+1)
            elif i-1<0:
                if matrica[i+1][j]>broj and matrica[i][j+1]>broj and matrica[i][j-1]>broj:
                    suma+=(broj+1)
            elif j+1>=len(matrica[i]):
                if matrica[i+1][j]>broj and matrica[i-1][j]>broj and matrica[i][j-1]>broj:
                    suma+=(broj+1)
            elif j-1<0:
                if matrica[i+1][j]>broj and matrica[i-1][j]>broj and matrica[i][j+1]>broj:
                    suma+=(broj+1)
            else:
                if matrica[i+1][j]>broj and matrica[i-1][j]>broj and matrica[i][j+1]>broj and matrica[i][j-1]>broj :
                    suma+=(broj+1)
    return (suma)

#puno bolji nacin napraviti Vrijednost funkciju i gledati
#da li se se nalazi u opsegu, nego pisati milion if-ova
def drugi_dio():
    basin = []

    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            brojac = 0
            otvorena_lista = [[i, j]]
            zatvorena_lista = []
            while len(otvorena_lista) > 0:
                if (otvorena_lista[0] not in zatvorena_lista) and Vrijednost(matrica, otvorena_lista[0]) < 9:
                    brojac += 1
                    zatvorena_lista.append(otvorena_lista[0])
                    ix = otvorena_lista[0][0]
                    iy = otvorena_lista[0][1]
                    for broj in [[ix + 1, iy], [ix - 1, iy], [ix, iy + 1], [ix, iy - 1]]:
                        otvorena_lista.append(broj)
                del (otvorena_lista[0])
            for broj in zatvorena_lista:
                matrica[broj[0]][broj[1]] = 9
            if brojac > 0:
                basin.append(brojac)

    basin = sorted(basin, reverse=True)
    return (basin[0] * basin[1] * basin[2])

print(prvi_dio())
print(drugi_dio())