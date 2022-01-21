from collections import defaultdict

def rotirajTacku(tacka, rotacija):
    x, y, z = tacka
    if rotacija == 0:
        return (x, y, z)
    if rotacija == 1:
        return (x, -z, y)
    if rotacija == 2:
        return (x, -y, -z)
    if rotacija == 3:
        return (x, z, -y)
    if rotacija == 4:
        return (-x, -y, z)
    if rotacija == 5:
        return (-x, -z, -y)
    if rotacija == 6:
        return (-x, y, -z)
    if rotacija == 7:
        return (-x, z, y)
    if rotacija == 8:
        return (y, x, -z)
    if rotacija == 9:
        return (y, -x, z)
    if rotacija == 10:
        return (y, z, x)
    if rotacija == 11:
        return (y, -z, -x)
    if rotacija == 12:
        return (-y, x, z)
    if rotacija == 13:
        return (-y, -x, -z)
    if rotacija == 14:
        return (-y, -z, x)
    if rotacija == 15:
        return (-y, z, -x)
    if rotacija == 16:
        return (z, x, y)
    if rotacija == 17:
        return (z, -x, -y)
    if rotacija == 18:
        return (z, -y, x)
    if rotacija == 19:
        return (z, y, -x)
    if rotacija == 20:
        return (-z, x, -y)
    if rotacija == 21:
        return (-z, -x, y)
    if rotacija == 22:
        return (-z, y, x)
    if rotacija == 23:
        return (-z, -y, -x)


def saberiTacke(tacka1, tacka2):
    x1, y1, z1 = tacka1
    x2, y2, z2 = tacka2
    return (x1 + x2, y1 + y2, z1 + z2)


def oduzmiTacke(tacka1, tacka2):
    x1, y1, z1 = tacka1
    x2, y2, z2 = tacka2
    return (x1 - x2, y1 - y2, z1 - z2)


def invertovanaTacka(tacka):
    x, y, z = tacka
    return (-x, -y, -z)


def ManhattanDistanca(tacka1, tacka2):
    x1, y1, z1 = tacka1
    x2, y2, z2 = tacka2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


f = open("input/19.txt")
data = f.read().strip().split("\n\n")
nizSkenera = []
for nizLinija in data:
    beacons = []
    for linija in nizLinija.split("\n"):
        if "--" not in linija:
            beacons.append(tuple([int(c) for c in linija.split(",")]))
    nizSkenera.append(beacons)
citavOkean = set(nizSkenera.pop(0))
koordinateSkenera = [(0, 0, 0)]

while nizSkenera:
    prviSkener = nizSkenera.pop(0)
    flag = False
    for rotacija in range(24):
        offsets = defaultdict(int)
        for beacon in citavOkean:
            for tacka in prviSkener:
                rotiranaTacka = rotirajTacku(tacka, rotacija)
                x1, y1, z1 = beacon
                x2, y2, z2 = rotiranaTacka
                offset = oduzmiTacke(rotiranaTacka, beacon)
                offsets[offset] += 1
        for offset, ct in offsets.items():
            if ct >= 12:
                flag = True
                skener = invertovanaTacka(offset)
                koordinateSkenera.append(skener)
                for tacka in prviSkener:
                    tacka = rotirajTacku(tacka, rotacija)
                    citavOkean.add(saberiTacke(tacka, skener))
        continue
    if not flag:
        nizSkenera.append(prviSkener)
print(len(citavOkean))

udaljenostSkenera = set()
while koordinateSkenera:
    tacka1 = koordinateSkenera.pop()
    for tacka2 in koordinateSkenera:
        udaljenostSkenera.add(ManhattanDistanca(tacka1, tacka2))
print(max(udaljenostSkenera))