def prvi_dio():
    f = open("input/7.txt", "r")
    niz = []
    for x in f:
        niz = [int(broj) for broj in x.split(',') if broj.strip().isdigit()]
    nizSet = set(niz)
    suma = []
    for x in range(max(nizSet)):
        suma_temp=0
        for y in niz:
            suma_temp+=abs(y - x)
        suma.append(suma_temp)
    return (int(min(suma)))


def drugi_dio():
    f = open("input/7.txt", "r")
    niz=[]
    for x in f:
        niz=[int(broj) for broj in x.split(',') if broj.strip().isdigit()]
    nizSet=set(niz)
    suma=[]
    for x in range(max(nizSet)):
        suma_temp=0
        for y in niz:
            n=abs(y-x)
            suma_temp+=n*(n+1)
        suma.append(suma_temp/2)
    return (int(min(suma)))

print(prvi_dio())
print(drugi_dio())