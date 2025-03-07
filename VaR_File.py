# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Clg7jz8VObBaqHwaQS_oE87aZE0pGp9
"""

import numpy as np
from scipy.stats import norm


def VaR(r, confidence, principal=1):

    alpha = (1 - confidence) * 100
    var_percentile = np.percentile(r, alpha)
    out = principal * abs(var_percentile)
    return out