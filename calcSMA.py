import numpy as np
import pandas as pd

def calcSMA(df, prices, nos):
    """
    Calculates a simple moving average according to nos (number of steps).
    Edits the inputted dataframe in place. Returns nothing.

    :Inputs:
    * df: dataframe of trades
    * prices: price column from df
    * nos: number of steps
    """
    colName = 'SMA-%s' % nos
    df[colName] = float('NaN')
    df[colName].iloc[nos:] = [np.mean(prices.iloc[i-nos:i]) \
                              for i in range(nos,len(prices))]
