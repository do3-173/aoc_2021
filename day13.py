def prvi_dio():
    f = open("input/13.txt", "r")
    nizLinija = f.readlines()
    s = ""
    for red in nizLinija:
        s += red
    paroviKoordinata, savijanje = s.split("\n\n")
    savijanje=savijanje.split("\n")[0]
    tacke = set()
    for linija in paroviKoordinata.splitlines():
        x, y = list(map(int, linija.split(",")))
        tacke.add(complex(x, y))
    for linija in savijanje.splitlines():
        osa, x = linija.split(" ")[2].split("=")
        x = int(x)
        if osa == "y":
            ispodSredine = set(filter(lambda d: d.imag > x, tacke))
            tacke -= ispodSredine
            for b in ispodSredine:
                tacke.add(complex(b.real, x - (b.imag - x)))
        else:
            desnoSredina = set(filter(lambda d: d.real > x, tacke))
            tacke -= desnoSredina
            for r in desnoSredina:
                tacke.add(complex(x - (r.real - x), r.imag))
    return len(tacke)


def drugi_dio():
    f = open("input/13.txt", "r")
    nizLinija = f.readlines()
    s = ""
    for red in nizLinija:
        s += red
    paroviKoordinata, savijanje = s.split("\n\n")
    tacke = set()
    for linija in paroviKoordinata.splitlines():
        x, y = list(map(int, linija.split(",")))
        tacke.add(complex(x, y))
    for linija in savijanje.splitlines():
        osa, x = linija.split(" ")[2].split("=")
        x = int(x)
        if osa == "y":
            ispodSredine = set(filter(lambda d: d.imag > x, tacke))
            tacke -= ispodSredine
            for b in ispodSredine:
                tacke.add(complex(b.real, x - (b.imag - x)))
        else:
            desnoSredina = set(filter(lambda d: d.real > x, tacke))
            tacke -= desnoSredina
            for r in desnoSredina:
                tacke.add(complex(x - (r.real - x), r.imag))
    for y in range(0, 6):
        print("".join(["#" if complex(x, y) in tacke else " " for x in range(0, 39)]))
    return len(tacke)

print(prvi_dio())
print(drugi_dio())