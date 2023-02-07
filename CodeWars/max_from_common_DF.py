import pandas as pd
import numpy as np


def max_common(df_a, df_b):
    temp = df_a.combine(df_b, np.maximum)
    res = df_a.copy()
    for col_name in df_a.columns:
        if col_name in df_b.columns:
            res[col_name] = temp[col_name]
    return res


if __name__ == "__main__":
    df_1 = pd.DataFrame(((2.5, 2.0, 2.0),      (2.0, 2.0, 2.0)),      columns=["A", "B", "C"])
    df_2 = pd.DataFrame(((1.0, 6.0, 7.0, 1.0), (8.5, 1.0, 9.0, 1.0)), columns=["C", "B", "D", "E"])

    print(df_1, df_2, sep='\n')
    print(max_common(df_1, df_2))
