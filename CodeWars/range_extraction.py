def solution(args):
    temp = [[args[0]]]
    for i, val in enumerate(args):
        if i != 0:
            if val == args[i-1] + 1:
                temp[-1].append(val)
            else:
                temp.append([val])

    res = ''
    for r in temp:
        if len(r) == 1:
            res += f'{r[0]},'
        elif len(r) == 2:
            res += f'{r[0]},{r[1]},'
        elif len(r) > 2:
            res += f'{r[0]}-{r[-1]},'

    return res[:-1]


if __name__ == "__main__":
    print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
