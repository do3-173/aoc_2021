import copy

f= open("input/25.txt", "r")
data=f.readlines()

nizLinija = []
for x in data:
    linija = x.strip()
    niz = []
    for r in linija:
        niz.append(r)
    nizLinija.append(niz)

nizLinijaKopija = copy.deepcopy(nizLinija)
visina = len(nizLinijaKopija)
sirina = len(nizLinijaKopija[0])

flag = True
brojac = 0
while flag:
    flag = False
    pomjeren = False
    nizLinijaKopija1 = copy.deepcopy(nizLinijaKopija)
    for y in range(visina):
        for x in range(sirina):
            if nizLinijaKopija[y][x] == ">":
                if x < sirina - 1:
                    temp_x = x + 1
                else:
                    temp_x = 0
                if nizLinijaKopija[y][temp_x] == ".":
                    nizLinijaKopija1[y][x] = "."
                    nizLinijaKopija1[y][temp_x] = ">"
                    pomjeren = True
    nizLinijaKopija2 = copy.deepcopy(nizLinijaKopija1)
    for y in range(visina):
        for x in range(sirina):
            if nizLinijaKopija1[y][x] == "v":
                if y < visina - 1:
                    temp_y = y + 1
                else:
                    temp_y = 0
                if nizLinijaKopija1[temp_y][x] == ".":
                    nizLinijaKopija2[y][x] = "."
                    nizLinijaKopija2[temp_y][x] = "v"
                    pomjeren = True
    brojac += 1
    nizLinijaKopija = copy.deepcopy(nizLinijaKopija2)
    if pomjeren:
        flag = True

print(brojac)