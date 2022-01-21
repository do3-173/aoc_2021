import numpy as np

def skenerPovecaj(brojKoraka):
    f = open("input/20.txt", "r")
    nizLinija = f.read().strip()
    algoritam, slika = nizLinija.split('\n\n')
    alogitamBit = {}
    for i, vrijednost in enumerate(algoritam):
        if vrijednost == '#':
            alogitamBit[i] = 1
        else:
            alogitamBit[i] = 0

    slika = slika.split('\n')
    slikaBit = np.zeros((len(slika), len(slika[0])), dtype=int)

    for i, red in enumerate(slika):
        for j, vrijednost in enumerate(red):
            if vrijednost == '#':
                slikaBit[i, j] = 1
            else:
                slikaBit[i, j] = 0

    brojac = 1

    while brojac <= brojKoraka:
        if alogitamBit[1] == 1 and not brojac % 2:
            slikaPad = np.ones((slikaBit.shape[0] + 4,
                                 slikaBit.shape[1] + 4),
                                dtype=int)
        else:
            slikaPad = np.zeros((slikaBit.shape[0] + 4,
                                  slikaBit.shape[1] + 4),
                                 dtype=int)
        slikaPad[2:-2, 2:-2] = slikaBit
        nuleSlika = np.zeros((slikaBit.shape[0] + 2,
                            slikaBit.shape[1] + 2),
                           dtype=int)
        for lokacija, vrijednost in np.ndenumerate(slikaPad):
            x, y = lokacija
            if (x in range(1, len(slikaPad) - 1)
                    and y in range(1, len(slikaPad) - 1)):
                dioPixela = slikaPad[x - 1:x + 2, y - 1:y + 2]
                pixelString = ''
                for red in dioPixela:
                    for vrijednostStringa in red:
                        pixelString += str(vrijednostStringa)

                nuleSlika[x - 1, y - 1] = alogitamBit[int(pixelString, 2)]

        slikaBit = nuleSlika.copy()
        brojac += 1

    return np.count_nonzero(slikaBit)

print(skenerPovecaj(2))
print(skenerPovecaj(50))
