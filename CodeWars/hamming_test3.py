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
    for i in range(int(x**0.5)+1):
        if powerof**i == x:
            return True
    return False


HAMMINGS = []


def hamming(n):
    if not isinstance(n, int) or n < 1:
        raise IndexError('Index must be an integer and greater than zero')

    if n < len(HAMMINGS):
        return HAMMINGS[n-1]

    if HAMMINGS:
        num = HAMMINGS[-1] + 1
    else:
        num = 1

    while len(HAMMINGS) < n:

        if not( num % 2 == 0 or num % 3 == 0 or num % 10 in (0, 5) ):
            num += 1
            continue

        if is_powerof(num, 2) or is_powerof(num, 3) or is_powerof(num, 5):
            HAMMINGS.append(num)
            num += 1
            continue

        sq = num ** 0.5
        for div_l in range(int(sq), 1, -1):
            if num % div_l == 0:
                if div_l in HAMMINGS or is_powerof(div_l, 2) or is_powerof(div_l, 3) or is_powerof(div_l, 5):
                    div_r = num // div_l
                    if div_r in HAMMINGS or is_powerof(div_r, 2) or is_powerof(div_r, 3) or is_powerof(div_r, 5):
                        HAMMINGS.append(num)
                        break

        num += 1
    return HAMMINGS[-1]


print(hamming(300))
print(HAMMINGS)


# for i in range(1, 5000):
#     ham = hamming(i)
#     print(
#         ham,
#         # dividers(ham, ham)
#     )

# print(900)
# print(dividers(900, 900))