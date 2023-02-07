import pandas as pd
import numpy as np


def flatten(inp_df, col):
    res = inp_df.copy()

    for row in res.index:


    return res.reset_index()


if __name__ == '__main__':
    x = [
        [[1, 2], 5],
        [['a', 'b', 'c'], 6],
        [77, 3]
        ]

    df = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))

    df_expected = pd.DataFrame(data=[[1, 5], [2, 5], ['a', 6], ['b', 6], ['c', 6], [77, 3]], columns=list('AB'))

    print(df_expected)
    res = flatten(df, 'A')
    print(res)
    print(df_expected == df)