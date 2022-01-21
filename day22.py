from collections import defaultdict

f=open("input/22.txt").read()
nizLinija = f.strip().split("\n")

def volumenKocke(b):
    x1, x2 = b[0]
    y1, y2 = b[1]
    z1, z2 = b[2]
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) * (abs(z2 - z1) + 1)


def preklapanje(b1, b2):
    preklopljenaKocka = []
    for n1, n2 in zip(b1, b2):
        if n1[1] < n2[0] or n2[1] < n1[0]:
            return None
        graniceKocke = (max(n1[0], n2[0]), min(n1[1], n2[1]))
        preklopljenaKocka.append(graniceKocke)
    return tuple(preklopljenaKocka)

def prebroj(koraci):
    brojPrebrojanih = defaultdict(int)
    for i in range(len(koraci)):
        onOff, graniceKocke = koraci[i]
        promjeneMapa = defaultdict(int)
        kljucMapa = set(brojPrebrojanih.keys())
        for kocka in kljucMapa:
            preklopljenaKocka = preklapanje(graniceKocke, kocka)
            if not preklopljenaKocka:
                continue
            promjeneMapa[preklopljenaKocka] -= brojPrebrojanih[kocka]
        if onOff:
            promjeneMapa[graniceKocke] += 1
        for k in promjeneMapa:
            brojPrebrojanih[k] += promjeneMapa[k]
    return brojPrebrojanih

def prvi_dio():
    koraci = []
    for linija in nizLinija:
        onOff, koordinate = linija.split(" ")
        graniceKocke = tuple(tuple(int(p) for p in l[2:].split("..")) for l in koordinate.split(","))
        x, y, z = graniceKocke
        if (-50 <= int(x[0]) <= 50
        and -50 <= int(x[1]) <= 50
        and -50 <= int(y[0]) <= 50
        and -50 <= int(y[1]) <= 50
        and -50 <= int(z[0]) <= 50
        and -50 <= int(z[1]) <= 50):
            koraci.append((onOff == "on", graniceKocke))
    brojPrebrojanih = prebroj(koraci)
    ukljuceno = 0
    for kocka in brojPrebrojanih:
        ukljuceno += volumenKocke(kocka) * brojPrebrojanih[kocka]
    return ukljuceno

def drugi_dio():
    koraci = []
    for linija in nizLinija:
        onOff, koordinate = linija.split(" ")
        graniceKocke = tuple(tuple(int(p) for p in l[2:].split("..")) for l in koordinate.split(","))
        koraci.append((onOff == "on", graniceKocke))
    brojPrebrojanih = prebroj(koraci)
    ukljuceno = 0
    for kocka in brojPrebrojanih:
        ukljuceno += volumenKocke(kocka) * brojPrebrojanih[kocka]
    return ukljuceno

print(prvi_dio())
print(drugi_dio())