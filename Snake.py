# змейка по спирали

size = 3

tab = [[0]*size for row in range(size)]
tab[0] = [(col+1) for col in range(size)]

for line in tab:
    print("\t".join(map(str, line)))