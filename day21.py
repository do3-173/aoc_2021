from collections import defaultdict

pobjede = [0, 0]
pozicijaInput = [7, 6] #Rucno unesen input

def bacajKocke():
    bacanjeKocke = defaultdict(int)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                sumaBacanja = d1 + d2 + d3
                bacanjeKocke[sumaBacanja] += 1
    return bacanjeKocke

def partijaKocke(jednaPartija, univerzum, partije):
    (prviIgracPozicija, prviIgracRezultat), (drugiIgracPozicija, drugiIgracRezultat) = jednaPartija
    for jednoBacanje, prvoBacanjeUniverzuma in bacanjeKocke.items():
        prviIgracUniverzum = univerzum * prvoBacanjeUniverzuma
        prviIgracPozicija1 = prviIgracPozicija + jednoBacanje
        prviIgracPozicija1 = (prviIgracPozicija1 - 1) % 10 + 1
        prviIgracRezultat1 = prviIgracRezultat + prviIgracPozicija1
        if prviIgracRezultat1 >= 21:
            pobjede[0] += prviIgracUniverzum
        else:
            for drugoBacanje, drugoBacanjeUniverzuma in bacanjeKocke.items():
                drugiIgracUniverzum = prviIgracUniverzum * drugoBacanjeUniverzuma
                drugiIgracPozicija1 = drugiIgracPozicija + drugoBacanje
                drugiIgracPozicija1 = (drugiIgracPozicija1 - 1) % 10 + 1
                drugiIgracRezultat1 = drugiIgracRezultat + drugiIgracPozicija1
                if drugiIgracRezultat1 >= 21:
                    pobjede[1] += drugiIgracUniverzum
                else:
                    partije[((prviIgracPozicija1, prviIgracRezultat1), (drugiIgracPozicija1, drugiIgracRezultat1))] += drugiIgracUniverzum
    return

def odigrajPartiju(partije):
    while len(partije) > 0:
        partijeRunda = dict(partije)
        partije = defaultdict(int)
        for trenutnoStanje, univerzum in partijeRunda.items():
            partijaKocke(trenutnoStanje, univerzum, partije)
    return pobjede

bacanjeKocke = bacajKocke()
partije = defaultdict(int)
trenutnoStanje = ((pozicijaInput[0], 0), (pozicijaInput[1], 0))
partije[trenutnoStanje] = 1
print(max(odigrajPartiju(partije)))
