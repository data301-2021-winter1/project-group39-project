import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
def df_percentage(df,case_column,death_column,new_column):
    """
    Adds a column for the percent deaths of a certain demographic of people
    
    parameters
    ---------
    df: dataframe you're pulling from
    case_column: The living column numbers
    death_column: The dead column numbers
    new_column: The name you want the percent column to be 
    
    Results
    -------
    Made a column for the percent of people diagnosed who died
    """
    df[new_column] = df[death_column]/df[case_column]
    return df

##Having a load and clean function didn't make sense as there was only one method chain


