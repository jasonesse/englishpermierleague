import pandas as pd

def source_load(debug=False, filename = 'epl2020.csv'):
    source_df = pd.read_csv(f'.\data\{filename}')
    if debug:
        from explore.inspect import show_df
        show_df(source_df)
    return source_df