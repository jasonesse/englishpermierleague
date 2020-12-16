import pandas as pd

def source_load(debug=False):
    source_df = pd.read_csv('.\data\epl2020.csv')
    if debug:
        from explore.inspect import show_df
        show_df(source_df)
    return source_df