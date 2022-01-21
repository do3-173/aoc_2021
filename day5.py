def razmakTacaka(p1, p2):
    if p1 > p2:
        korak = -1
        p2 -= 1
    else:
        korak = 1
        p2 += 1
    return p1, p2, korak

def crtajLiniju(diagram, prvaTacka, drugaTacka, prviDio=True):
    x1, y1 = map(int, prvaTacka.split(','))
    x2, y2 = map(int, drugaTacka.split(','))
    if x1 == x2 and y1 == y2:
        if diagram.get(prvaTacka):
            diagram[prvaTacka] += 1
        else:
            diagram[prvaTacka] = 1
    elif x1 == x2:
        p1, p2, dy = razmakTacaka(y1, y2)
        for y in range(p1, p2, dy):
            tacka=f'{x1},{y}'
            if diagram.get(tacka):
                diagram[tacka] += 1
            else:
                diagram[tacka] = 1

    elif y1 == y2:
        p1, p2, dx = razmakTacaka(x1, x2)
        for x in range(p1, p2, dx):
            tacka=f'{x},{y1}'
            if diagram.get(tacka):
                diagram[tacka] += 1
            else:
                diagram[tacka] = 1
    elif abs(x1 - x2) == abs(y1 - y2) and prviDio:
        px1, px2, dx = razmakTacaka(x1, x2)
        p1, p2, dy = razmakTacaka(y1, y2)
        for i in range(px1, px2, dx):
            tacka = f'{x1},{y1}'
            if diagram.get(tacka):
                diagram[tacka] += 1
            else:
                diagram[tacka] = 1
            x1 += dx
            y1 += dy
    else:
        pass


diagram = {}
f=open("input/5.txt")
nizLinija=f.readlines()
prviDio=True
for linija in nizLinija:
    prvaTacka, drugaTacka = linija.replace('\n', '').split(' -> ')
    crtajLiniju(diagram, prvaTacka, drugaTacka,prviDio)
vrijednostiDijagrama = list(diagram.values())
preklapanje = len(vrijednostiDijagrama) - vrijednostiDijagrama.count(1)
print(preklapanje)
