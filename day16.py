import math

f=open("input/16.txt")
linija=f.read()
bits = bin(int('1'+open("input/16.txt").read(),16))[3:]


operacije = [sum,
             math.prod,
             min,
             max,
             lambda lam: lam[0], # literal
             lambda lam: 1 if lam[0] > lam[1] else 0,  # vece
             lambda lam: 1 if lam[0] < lam[1] else 0,  # manje
             lambda lam: 1 if lam[0] == lam[1] else 0] # jednako

def prvi_dio(pocetniBit):
    i = pocetniBit
    verzija = int(bits[i:i+3],2)
    ID = int(bits[i+3:i+6],2)
    i += 6
    if ID == 4:
        while True:
            i += 5
            if bits[i-5] == '0':
                break
    else:
        if bits[i] == '0':
            krajodi = i + 16 + int(bits[i+1:i+16],2)
            i += 16
            while i < krajodi:
                i,v = prvi_dio(i)
                verzija += v
        else:
            brojSubpackets = int(bits[i+1:i+12],2)
            i += 12
            for j in range(brojSubpackets):
                i,v = prvi_dio(i)
                verzija += v
    return i,verzija

def drugi_dio(pocetniBit):
    i = pocetniBit 
    ID = int(bits[i+3:i+6],2) 
    i += 6
    if ID == 4:
        vrijednosti = [0]
        while True:
            vrijednosti[0] = 16*vrijednosti[0] + int(bits[i+1:i+5],2)
            i += 5
            if bits[i-5] == '0':
                break
    else:
        vrijednosti = []
        if bits[i] == '0':
            krajodi = i + 16 + int(bits[i+1:i+16],2)
            i += 16
            while i < krajodi:
                i,v = drugi_dio(i)
                vrijednosti.append(v)
        else:
            brojSubpackets = int(bits[i+1:i+12],2)
            i += 12
            for j in range(brojSubpackets):
                i,v = drugi_dio(i)
                vrijednosti.append(v)
    return i,operacije[ID](vrijednosti)

print(prvi_dio(0)[1])
print(drugi_dio(0)[1])