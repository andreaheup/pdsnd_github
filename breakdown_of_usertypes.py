# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:36:44 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

# load data file into a dataframe
df = pd.read_csv("chicago.csv")
user_counts = df['User Type'].value_counts()
