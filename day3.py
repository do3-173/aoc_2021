def prvi_dio():
    f = open("input/3.txt", "r")
    niz=[]
    niz0=[]
    niz1=[]
    for x in f:
        niz.append(x)
    for x in range((len(niz[0])-1)):
        niz0.append(0)
        niz1.append(0)
        for y in niz:
            if y[x]=="0":
                niz0[x]+=1
            else:
                niz1[x]+=1
    gamma=epsilon=""
    for x in range((len(niz[0])-1)):
        if(niz0[x]>niz1[x]):
            gamma+="0"
            epsilon+="1"
        else:
            gamma += "1"
            epsilon += "0"
    return (int(gamma,2)*int(epsilon,2))

def drugi_dio():
    f = open("input/3.txt", "r")

    niz = []

    for x in f:
        niz.append(x)

    niz_1 = niz_0 = niz

    for x in range((len(niz[0]) - 1)):
        niz0 = []
        niz1 = []
        for y in niz_1:
            if y[x] == "0":
                niz0.append(y)
            else:
                niz1.append(y)
        if (len(niz1) >= len(niz0) and len(niz1) != 0 and len(niz0) != 0):
            niz_1 = niz1
        else:
            niz_1 = niz0
        if(len(niz_1)==1):
            break

    for x in range((len(niz[0]) - 1) - 1):
        niz0 = []
        niz1 = []
        for y in niz_0:
            if y[x] == "0":
                niz0.append(y)
            else:
                niz1.append(y)
        if (len(niz0) <= len(niz1) and len(niz1) >= 1 and len(niz0) >= 1):
            niz_0 = niz0
        else:
            niz_0 = niz1
        if(len(niz_0)==1):
            break

    return (int(niz_0[0], 2) * int(niz_1[0], 2))

print(prvi_dio())
print(drugi_dio())

