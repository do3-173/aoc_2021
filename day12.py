from collections import defaultdict

def prvi_dio():
    f = open("input/12.txt", "r")
    nizLinija = f.readlines()
    cvor = defaultdict(set)
    for linija in nizLinija:
        lhs, rhs = linija.strip().split("-", maxsplit=2)
        cvor[lhs].add(rhs)
        cvor[rhs].add(lhs)

    def DFS(trenutniCvor, putanja):
        if trenutniCvor == "end":
            yield putanja
        else:
            for sljedeci in cvor[trenutniCvor]:
                if sljedeci == "start":
                    pass
                elif sljedeci.isupper() or sljedeci not in putanja:
                    yield from DFS(sljedeci, putanja + [sljedeci])

    return sum(1 for i in DFS("start", ["start"]))


def drugi_dio():
    f = open("input/12.txt", "r")
    nizLinija = f.readlines()
    flag=True
    cvor = defaultdict(set)
    for linija in nizLinija:
        lhs, rhs = linija.strip().split("-", maxsplit=2)
        cvor[lhs].add(rhs)
        cvor[rhs].add(lhs)

    def DFS(trenutniCvor, putanja, flag):
        if trenutniCvor == "end":
            yield putanja
        else:
            for sljedeci in cvor[trenutniCvor]:
                if sljedeci == "start":
                    pass
                elif sljedeci.isupper() or sljedeci not in putanja:
                    yield from DFS(sljedeci, putanja + [sljedeci], flag)
                elif flag and sljedeci.islower():
                    yield from DFS(sljedeci, putanja + [sljedeci], False)

    return sum(1 for i in DFS("start", ["start"], flag))

print(prvi_dio())
print(drugi_dio())
