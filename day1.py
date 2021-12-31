def prvi_dio():
    f = open("input/1.txt", "r")
    nizLinija=f.readlines()
    niz=[int(x.strip()) for x in nizLinija]
    prvi = True
    brojac = 0
    prethodni = 0
    for x in niz:
        if prvi:
            prvi = False
        else:
            if prethodni < x:
                brojac += 1
        prethodni = x
    return brojac

def drugi_dio():
    f = open("input/1.txt", "r")
    nizLinija=f.readlines()
    niz=[int(x.strip()) for x in nizLinija]
    prvi=drugi=treci=True
    brojac=1
    prethodni1=prethodni2=prethodni3=0
    suma=[]

    for x in niz:
      if prvi:
          prvi=False
          prethodni1 = x
      elif drugi:
          drugi=False
          prethodni2=x
      elif treci:
          treci=False
          prethodni3=x
      else:
          suma.append(int(prethodni1)+int(prethodni2)+int(prethodni3))
          prethodni1=prethodni2
          prethodni2=prethodni3
          prethodni3=x
    prvi=True
    prethodni=0
    for x in suma:
        if prvi:
            prvi = False
        else:
            if prethodni < x:
                brojac += 1
        prethodni = x

    return brojac

print(prvi_dio())
print(drugi_dio())