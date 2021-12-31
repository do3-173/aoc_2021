def solver(broj_iteracija):
    f = open("input/6.txt", "r")
    niz=[]
    for x in f:
        niz=[int(broj) for broj in x.split(',') if broj.strip().isdigit()]
    brojacRiba=[0,0,0,0,0,0,0,0,0]
    for i in range(len(niz)):
        brojacRiba[niz[i]]+=1
    temp=0
    for x in range(broj_iteracija):
        brojacRiba[8]=temp
        temp=brojacRiba[0]
        for y in range(8):
            brojacRiba[y]=brojacRiba[y+1]
        brojacRiba[6]  += temp

    suma=0
    for i in range(8):
        suma+=brojacRiba[i]
    return (suma)

print(solver(81))
print(solver(257))