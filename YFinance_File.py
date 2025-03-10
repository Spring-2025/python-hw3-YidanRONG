# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Clg7jz8VObBaqHwaQS_oE87aZE0pGp9
"""

import numpy as np
import pandas as pd

def YahooData2returns(YahooData):

    if 'Adj Close' not in YahooData:
        raise ValueError("YahooData must contain 'Adj Close' column.")

    pricevec = YahooData['Adj Close'].values
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns