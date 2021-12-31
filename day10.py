def prvi_dio():
    f = open("input/10.txt", "r")

    nizLinija = f.readlines()
    matrica = []
    for i in range(len(nizLinija)):
        niz = []
        for j in range(len(nizLinija[i]) - 1):
            niz.append(nizLinija[i][j])
        matrica.append(niz)

    nizKaraktera = ['(', ')', '[', ']', '{', '}', '<', '>']
    nizBrojacError = [0, 0, 0, 0]
    k = [3, 57, 1197, 25137]
    for red in matrica:
        nizBrojac = [0, 0, 0, 0, 0, 0, 0, 0]
        otvoreneZagrade = []
        flag = False
        for x in red:
            for i in range(len(nizKaraktera)):
                if x == nizKaraktera[i]:
                    nizBrojac[i] += 1
                    if i % 2 == 0:
                        otvoreneZagrade.append(x)
                    else:
                        if nizBrojac[i - 1] < nizBrojac[i] or otvoreneZagrade[len(otvoreneZagrade) - 1] != nizKaraktera[
                            i - 1]:
                            j = int((i - 1) / 2)
                            nizBrojacError[j] += 1
                            flag = True
                        else:
                            del otvoreneZagrade[len(otvoreneZagrade) - 1]
                if flag:
                    break
            if flag:
                break
    suma = 0
    for i in range(len(k)):
        suma += nizBrojacError[i] * k[i]
    return (suma)


def drugi_dio():
    f = open("input/10.txt", "r")

    nizLinija = f.readlines()
    matrica = []
    for i in range(len(nizLinija)):
        niz = []
        for j in range(len(nizLinija[i]) - 1):
            niz.append(nizLinija[i][j])
        matrica.append(niz)

    nizKaraktera = ['(', ')', '[', ']', '{', '}', '<', '>']
    nizBrojacError = [0, 0, 0, 0]
    suma = []
    k = [3, 57, 1197, 25137]
    for red in matrica:
        incompleteString = ""
        nizBrojac = [0, 0, 0, 0, 0, 0, 0, 0]
        otvoreneZagrade = []
        flag = False
        for x in red:
            for i in range(len(nizKaraktera)):
                if x == nizKaraktera[i]:
                    nizBrojac[i] += 1
                    if i % 2 == 0:
                        otvoreneZagrade.append(x)
                    else:
                        if nizBrojac[i - 1] < nizBrojac[i] or otvoreneZagrade[len(otvoreneZagrade) - 1] != nizKaraktera[
                            i - 1]:
                            j = int((i - 1) / 2)
                            nizBrojacError[j] += 1
                            flag = True
                        else:
                            del otvoreneZagrade[len(otvoreneZagrade) - 1]
                if flag:
                    break
            if flag:
                break
        if flag:
            continue

        while len(otvoreneZagrade) > 0:
            for i in range(len(nizKaraktera)):
                if nizKaraktera[i] == otvoreneZagrade[len(otvoreneZagrade) - 1]:
                    incompleteString += nizKaraktera[i + 1]
                    del otvoreneZagrade[len(otvoreneZagrade) - 1]
                    break
        suma_temp = 0
        for c in incompleteString:
            suma_temp *= 5
            if c == ')':
                suma_temp += 1
            elif c == ']':
                suma_temp += 2
            elif c == '}':
                suma_temp += 3
            elif c == '>':
                suma_temp += 4
        suma.append(suma_temp)

    suma = sorted(suma)
    return (suma[int(len(suma) / 2)])


print(prvi_dio())
print(drugi_dio())
