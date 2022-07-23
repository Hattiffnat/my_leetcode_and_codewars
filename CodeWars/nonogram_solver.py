import numpy as np


class Nonogram:
    def __init__(self, clues):
        self.columns = clues[0]
        self.rows = clues[1]
        self.shape = (len(self.rows), len(self.columns))
        self.arr = np.full(self.shape, 3, dtype=int)

    # def to_str(self, tup):
    #     return ''.join(tup)
    #
    # def to_tup(self, s):
    #     return tuple(s)

    def solve(self):
        for i in range(self.shape[0]):
            if '3' in self.arr[i, :]:
                if self.check_seq(self.rows[i], self.arr[i, :]):

                    res = self.check_clue(self.rows[i], axis=0)
                    if res is not None:
                        self.arr[i, :] = res

    def check_seq(self, clue:tuple, seq:list) -> bool:
        if tuple([len(i) for i in str(seq.replace('3', '0')).split('0')]) == clue:
            return True
        return False

    def check_clue(self, clue, axis):
        s = '0'.join(['1'*i for i in clue])
        if len(s) == self.shape[axis]:
            return tuple(s)
        else:
            return None



clues = (
    ((1, 1), (4,), (1, 1, 1), (3,), (1,)),
    ((1,), (2,), (3,), (2, 1), (4,))
)

test = Nonogram(clues)
print(test.solve())

ans = (
    (0, 0, 1, 0, 0),
    (1, 1, 0, 0, 0),
    (0, 1, 1, 1, 0),
    (1, 1, 0, 1, 0),
    (0, 1, 1, 1, 1),
)