from itertools import permutations


HAMMINGS = []


def hamming(n):
    global HAMMINGS
    if n < len(HAMMINGS):
        return HAMMINGS[n-1]

    d = 7 if n < 100 else 1

    while d**3 < n: d += 1

    alph = []
    for i in range(d):
        alph += [i] * 3

    res = [i for i in permutations(alph, 3)]
    for i in range(len(res)):
        res[i] = ' '.join([str(j) for j in res[i]])
    res = list(set(res))

    hamm = []
    for i in res:
        comb = [int(k) for k in i.split(' ')]
        hamm.append( 2**comb[0] * 3**comb[1] * 5**comb[2] )

    hamm.sort()
    print(hamm)

    if len(HAMMINGS) < len(hamm):
        HAMMINGS = hamm

    return hamm[n-1]


hamming(10)

# for i in range(1, 5000):
#     print(hamming(i))

