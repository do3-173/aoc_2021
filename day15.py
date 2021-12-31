from heapq import heappop, heappush

#Heap queue algoritam, binarno stablo gdje svaki roditelj ima manju ili jednaku vrijednost od svog djeteta.
#Koristi se zbog Dijkstra algoritma

f = open("input/15.txt", "r")

nizLinija=f.read()
data = [list(map(int, red)) for red in nizLinija.strip().split("\n")]


def najkracaDistanca(velicinaPecine):
    heap = [(0, 0, 0)]
    posjecen = {(0, 0)}
    while heap:
        udaljenost, x, y = heappop(heap)
        if x == velicinaPecine * len(data) - 1 and y == velicinaPecine * len(data[0]) - 1:
            return udaljenost

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x1, y1 = x + dx, y + dy
            if x1 < 0 or y1 < 0 or x1 >= velicinaPecine * len(data) or y1 >= velicinaPecine * len(data):
                continue

            a, am = divmod(x1, len(data))
            b, bm = divmod(y1, len(data[0]))
            n = ((data[am][bm] + a + b) - 1) % 9 + 1

            if (x1, y1) not in posjecen:
                posjecen.add((x1, y1))
                heappush(heap, (udaljenost + n, x1, y1))


print(najkracaDistanca(1))
print(najkracaDistanca(5))