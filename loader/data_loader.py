import pandas as pd
from pandasgui import show

def source_load(debug=False):
    source_df = pd.read_csv('.\data\epl2020.csv')
    if debug:
        show(source_df)
    return source_df