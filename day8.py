f = open("input/8.txt", "r")
nizLinija=f.readlines()

def format(linija):
    return list(map(lambda w: ''.join(sorted(w)), linija))

nizPrviDio = list(map(format, [linija.split('|')[0].strip().split() for linija in nizLinija]))
nizDrugiDio = list(map(format, [linija.split('|')[1].strip().split() for linija in nizLinija]))

nizDesifrovanih = []
mapiranjeSegmenata = {2: 1, 3: 7, 4: 4, 7: 8}
for linija in nizPrviDio:
    temp = {}
    for rijec in linija:
        if len(rijec) in mapiranjeSegmenata:
            temp[mapiranjeSegmenata[len(rijec)]] = rijec

    for rijec in linija:
        if len(rijec) == 6 and any(char not in rijec for char in temp[1]):
            temp[6] = rijec
            break
    for rijec in linija:
        if len(rijec) == 6 and any(char not in rijec for char in temp[4]) and rijec not in temp.values():
            temp[0] = rijec
            break
    for rijec in linija:
        if len(rijec) == 6 and rijec not in temp.values():
            temp[9] = rijec
            break
    for rijec in linija:
        if len(rijec) == 5 and all(char in temp[6] for char in rijec):
            temp[5] = rijec
            break

    for rijec in linija:
        if len(rijec) == 5 and all(char in temp[9] for char in rijec) and rijec not in temp.values():
            temp[3] = rijec
            break

    for rijec in linija:
        if len(rijec) == 5 and rijec not in temp.values():
            temp[2] = rijec
    nizDesifrovanih.append({v: k for k, v in temp.items()})
suma = 0
print(nizDesifrovanih)
for i, izlaz in enumerate(nizDrugiDio):
    suma += int(''.join(map(str, [nizDesifrovanih[i][rijec] for rijec in izlaz])))
print(suma)