# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:32:55 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
df = pd.read_csv("chicago.csv")
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())
print(df['Gender'].value_counts())
print(df['Birth Year'].value_counts())
