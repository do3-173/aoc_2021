from heapq import heappop, heappush

f= open("input/23.txt", "r")
nizLinija=f.readlines()
burrow=''
brojac=0
for linija in nizLinija:
    if brojac == 3:
        burrow += "DCBADBAC"
    for c in linija:
        if c in 'ABCD.':
            burrow+=c
    brojac+=1
print(burrow)


def mozeIzaci(burrow, pozicijaSobe):
    for a in pozicijaSobe:
        if burrow[a] == '.': 
            continue
        return a


def blokiran(a, b, burrow):
    korak = 1 if a < b else -1
    for pos in range(a + korak, b + korak, korak):
        if burrow[pos] != '.':
            return True


def potencijalnaPozicija(a, parc, burrow):
    for b in [pos for pos in parc if burrow[pos] == '.']:
        if blokiran(a, b, burrow): 
            continue
        yield b


def pomjeri(a, b, burrow):
    p = list(burrow)
    p[a], p[b] = p[b], p[a]
    povratni=''
    for c in p:
        povratni+=c
    return povratni


def mozeUci(a, b, amphipod, burrow, pozicijaSobe):
    for pos in pozicijaSobe:
        if burrow[pos] == '.':
            best_pos = pos
        elif burrow[pos] != amphipod:
            return False
    if not blokiran(a, b, burrow): return best_pos


def potencijalniPotezi(burrow, parc, korakIzlaska, krajnjiCilj):
    for a in [pos for pos in parc if burrow[pos] != '.']:
        amphipod = burrow[a]
        if (b := mozeUci(a, korakIzlaska[amphipod], amphipod, burrow, krajnjiCilj[amphipod])):
            yield a, b
    for room in 'ABCD':
        if not (a := mozeIzaci(burrow, krajnjiCilj[room])): continue
        for b in potencijalnaPozicija(korakIzlaska[room], parc, burrow):
            yield a, b


def solver(burrow):
    mapaAmphipod = dict(A=1, B=10, C=100, D=1000)
    parc = [0, 1, 3, 5, 7, 9, 10]
    korakIzlaska = dict(A=2, B=4, C=6, D=8)
    krajnjiCilj = {r: range(ord(r) - 54, len(burrow), 4) for r in 'ABCD'}
    krajnjiCiljI = {v: kljuc for kljuc, vrijednost in krajnjiCilj.items() for v in vrijednost}
    rjesenje = '.' * 11 + 'ABCD' * ((len(burrow) - 11) // 4)
    heap = [(0, burrow)]
    vidjen = {burrow: 0}
    while heap:
        utrosenoEnergije, trenutnoStanje = heappop(heap)
        if trenutnoStanje == rjesenje:
            return utrosenoEnergije
        for a, b in potencijalniPotezi(trenutnoStanje, parc, korakIzlaska, krajnjiCilj):
            p, r = (a, b) if a < b else (b, a)
            udaljenost = abs(korakIzlaska[krajnjiCiljI[r]] - p) + (r - 7) // 4
            utrosenoEnergije2 = utrosenoEnergije + udaljenost * mapaAmphipod[trenutnoStanje[a]]
            pomjerenoStanje = pomjeri(a, b, trenutnoStanje)
            if vidjen.get(pomjerenoStanje, 9999999) <= utrosenoEnergije2:
                continue
            vidjen[pomjerenoStanje] = utrosenoEnergije2
            heappush(heap, (utrosenoEnergije2, pomjerenoStanje))

print(solver(burrow))