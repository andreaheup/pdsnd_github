# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:34:04 2022

@author: Heup.Andrea
"""

import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

df = pd.read_csv('chicago.csv')

# create dataframe groupby
x = df.groupby(['Start Station', 'End Station'])

# find max value index in size of each groupby groups
popular_comb = x.size().idxmax()

# find size of max. comb
popular_comb_count = x.size()[popular_comb]

print(popular_comb[0], popular_comb[1])
print(popular_comb_count)
#result is Lake Shore Dr & Monroe St	Streeter Dr & Grand Ave - count 854
