# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:29 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def raw_data_view(df,i):
    """
    Returns for each repetition i next 5 rows of the dataframe df. 
    i=1 - 1. repetition - rows 1-5 are returned
    i=2 - 2. repetition - rows 6-10 are returned
    etc.
    """
    return df.iloc[6*(i-1):6*i-1]