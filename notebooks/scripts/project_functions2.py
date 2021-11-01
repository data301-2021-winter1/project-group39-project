import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
def load_and_process(path):
    df1 = (
        pd.read_csv(path)
    )
    
    df2 = df1.drop(df1.columns[18:59],axis=1)
    df2 = df2.drop(df2.columns[0],axis=1)
    df2 = df2.drop(df2.columns[67:105],axis=1)
    df2 = df2.drop(df2.columns[26:64],axis=1)
    return df2

def get_ratio(df,col1,col2,new_colname):
    df[new_colname] = df[col1]/df[col2]

    return df
        