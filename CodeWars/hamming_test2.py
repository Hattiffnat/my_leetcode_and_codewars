def divs_around_sqrt(x, q=None):
    res = []
    start = x**0.5

    for i in range(start, x):
        if x % i == 0: res.append(i)
        if q is not None and len(res) > q: break

    for i in range(start-1, 0, -1):
        if x % i == 0: res.insert(0, i)
        if q is not None and len(res) > q * 2: break

    return tuple(res)


def dividers(x:int, stop=None) -> tuple:
    if stop is None: stop = x
    res = []
    for i in range(1, stop):
        if x%i == 0: res.append(i)
    return tuple(res)


def is_powerof(x, powerof):
    for i in range(int(x**0.5+1)):
        if powerof**i == x:
            return True
    return False


def hamming(n):
    hammings = []
    num = 1
    while len(hammings) < n:

        if is_powerof(num, 2) or is_powerof(num, 3) or is_powerof(num, 5):
            hammings.append(num)
            num += 1
            continue

        sq = num ** 0.5
        old_div_r = int(sq) + 1
        for div_l in range(int(sq), 1, -1):
            is_hamming = False
            if num % div_l == 0:
                if div_l in hammings or is_powerof(div_l, 2) or is_powerof(div_l, 3) or is_powerof(div_l, 5):
                    for div_r in range(old_div_r, num):
                        if div_r * div_l == num:
                            old_div_r = div_r
                            if div_r in hammings or is_powerof(div_r, 2) or is_powerof(div_r, 3) or is_powerof(div_r, 5):
                                is_hamming = True
                                hammings.append(num)
                                break
            if is_hamming:
                break

        num += 1
    return hammings[-1]


for i in range(1, 5000):
    ham = hamming(i)
    print(
        ham,
        dividers(ham, ham),
        # f'{ham**0.5} -> {int(ham**0.5)}'
    )

# print(900)
# print(dividers(900, 900))