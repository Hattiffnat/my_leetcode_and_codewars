
def dividers(x:int, stop:int) -> tuple:
    res = []
    for i in range(2, stop):
        if x%i == 0: res.append(i)
    return tuple(res)


def is_powerof(x, powerof):
    for i in range(int(x**0.5+1)):
        if powerof**i == x:
            return True
    return False


def hamming(n):
    # first9 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    # if n < len(first9):
    #     return (first9[n - 1])
    #
    # clock = 8
    i = 1
    clock = 0
    res = None
    while clock < n:
        if is_powerof(i, 2) or is_powerof(i, 3) or is_powerof(i, 5):
            clock += 1
            res = i
            i += 1
            continue
        # dividers
        powered_divs = 0
        # for num in range(2, int(i ** 0.5) + 1):
        for num in range(2, i+1):

            if i % num == 0:
                if is_powerof(num, 2): powered_divs += 1
                if is_powerof(num, 3): powered_divs += 1
                if is_powerof(num, 5): powered_divs += 1
            if powered_divs > 1:
                clock += 1
                res = i
                # print('DEBUG hamming?:',i)
                break
        i += 1
    return res


for i in range (1, 40):
    ham = hamming(i)
    print(ham, dividers(ham, ham), ham**0.5)
