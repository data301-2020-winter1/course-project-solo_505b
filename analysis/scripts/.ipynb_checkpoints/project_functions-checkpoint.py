import pandas as pd
import numpy as np,

def load_and_process(url_or_path_to_csv_file):

    df =(pd.read_csv('../data/raw/framingham.csv',sep =',')
         .drop(['education'],axis=1,inplace=True)
         .rename(columns={'male':'Sex'},inplace=True)
         .dropna(axis=0,inplace=True)
        )
    return df