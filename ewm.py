import pandas as pd

def exponential_weighted_average(df, SMA, price, nos):
    colName = 'EWM-%s' % nos
    k = (2.0/nos) + 1
    df[colName] = float('NaN')
    df[colName].iloc[nos] = ((price.iloc[nos]-SMA.iloc[nos])*k) + SMA.iloc[nos]
    ewm = df[colName]
    for i in range(nos, len(ewm)-1):
        df[colName].iloc[(i+1)] = (((price.iloc[i+1]-ewm.iloc[i])*k) + ewm.iloc[i]) 