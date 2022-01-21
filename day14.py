from collections import Counter, defaultdict

f=open('input/14.txt')
nizTemplate, pravilaUmetanja = f.read().split('\n\n')
template = nizTemplate.strip()
izmedju = {}

for pravilo in pravilaUmetanja.split('\n'):
    par, slovo = pravilo.split(' -> ')
    izmedju[par] = slovo

def solver(koraci):
    n = len(template)
    mapaParova = defaultdict(int)
    brojac = Counter(template)

    for i in range(1, n):
        mapaParova[template[i - 1] + template[i]] += 1

    for i in range(koraci):
        noviPar = defaultdict(int)

        for par in list(mapaParova):
            if mapaParova[par] == 0:
                continue

            if par in izmedju:
                brojac[izmedju[par]] += mapaParova[par]
                noviPar[par[0] + izmedju[par]] += mapaParova[par]
                noviPar[izmedju[par] + par[1]] += mapaParova[par]

        mapaParova = noviPar

    return max(brojac.values()) - min(brojac.values())


print(solver(10))
print(solver(40))