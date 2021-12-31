#input unesen rucno
inputMin_X = 265
inputMax_X = 287
inputMin_Y = -103
inputMax_Y = -58

def simulacijaKosogHica(dx, dy):
    x = y = maxVisina = 0
    while y >= inputMin_Y:
        x += dx
        y += dy
        dx += -1 if dx > 0 else 1 if dx < 0 else 0
        dy += -1
        maxVisina = max(maxVisina, y)
        if inputMin_X <= x <= inputMax_X and inputMin_Y <= y <= inputMax_Y:
            return True, maxVisina
    return False, 0


def prvi_dio():
    maxVisina = 0
    for i in range(inputMax_X + 1):
        for j in range(-inputMin_Y):
            flagPogodio, visina = simulacijaKosogHica(i, j)
            if flagPogodio:
                maxVisina = max(maxVisina, visina)
    return maxVisina


def drugi_dio():
    brojac = 0
    for i in range(inputMax_X + 1):
        for j in range(inputMin_Y, -inputMin_Y):
            flagPogodio, visina = simulacijaKosogHica(i, j)
            brojac += flagPogodio
    return brojac


print(prvi_dio())
print(drugi_dio())