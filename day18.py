from copy import deepcopy

f= open("input/18.txt", "r")
nizLinija=f.readlines()
nizBrojeva = []
for linija in nizLinija:
    nizBrojeva.append(eval(linija))

def dodajSnailfish(x, y):
    return smanjiSnailFish([x, y])


def smanjiSnailFish(inputPar):
    inputPar = deepcopy(inputPar)
    while solver(inputPar):
        pass
    return inputPar


def solver(inputPar):
    parLijevo, iLijevo = None, None
    parDesno, iDesno = None, None
    parSplit, iSplit = None, None

    stack = [(0, [inputPar, None], 0)]

    while stack:
        dubina, par, i = stack.pop()
        if isinstance(par[i], int):
            if not parSplit and par[i] >= 10:
                parSplit, iSplit = par, i
            parLijevo, iLijevo = par, i
        else:
            if dubina >= 4:
                if stack:
                    dubinaNova, parDesno, iDesno = stack.pop()
                    while isinstance(parDesno[iDesno], list):
                        parDesno, iDesno = parDesno[iDesno], 0

                # explodiraj
                if parLijevo:
                    parLijevo[iLijevo] += par[i][0]
                if parDesno:
                    parDesno[iDesno] += par[i][1]
                par[i] = 0

                return True
            else:
                stack.append((dubina + 1, par[i], 1))
                stack.append((dubina + 1, par[i], 0))
    if parSplit:
        parSplit[iSplit] = [parSplit[iSplit] // 2, (parSplit[iSplit] + 1) // 2]
        return True
    return False


def magnitudaSnailfish(lista):
    if isinstance(lista, int):
        return lista
    else:
        return 3 * magnitudaSnailfish(lista[0]) + 2 * magnitudaSnailfish(lista[1])

x = nizBrojeva[0]
for y in nizBrojeva[1:]:
    x = dodajSnailfish(x, y)

print(magnitudaSnailfish(x))

maxSuma = 0
for i, a in enumerate(nizBrojeva):
    for j, b in enumerate(nizBrojeva):
        if i == j:
            continue
        maxSuma = max(maxSuma, magnitudaSnailfish(dodajSnailfish(a, b)))

print(maxSuma)