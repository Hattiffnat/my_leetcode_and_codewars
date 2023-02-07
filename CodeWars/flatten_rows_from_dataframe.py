import pandas as pd
import numpy as np


def flatten(inp_df, col):
    res = pd.DataFrame(columns=inp_df.columns, dtype=object)

    for row in inp_df.index:
        item = inp_df.loc[row, col]
        if type(item) not in (list,):
            res.loc[len(res)] = inp_df.iloc[row]
        else:
            arr = np.repeat([inp_df.iloc[row].values], len(item), axis=0)
            temp = pd.DataFrame(arr, columns=res.columns)
            temp[col] = item
            res = pd.concat((res, temp), axis=0, ignore_index=True)

    for column in res.columns:
        if column != col:
            res[column] = res[column].astype(np.int64)

    return res.sort_index().reset_index(drop=True).sort_index(axis=1)


if __name__ == '__main__':
    x = [
        [[1, 2], 5],
        [['a', 'b', 'c'], 6],
        [77, 3]
        ]

    df = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))

    df_expected = pd.DataFrame(data=[[1, 5], [2, 5], ['a', 6], ['b', 6], ['c', 6], [77, 3]], columns=list('AB'))

    # print(df_expected)
    res = flatten(df, 'A')
    # print(res)

    print(df_expected.info())
    print(res.info())

    print(df_expected == res)
