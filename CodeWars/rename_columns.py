import pandas as pd


def rename_columns(df, names):
    res = df.copy()
    res.columns = names
    return res


if __name__ == "__main__":
    df = pd.DataFrame(((1,2,3), (4,5,6)))
    print(df)
    rename_columns(df, ['A', 'B', 'C'])
    print(df)
