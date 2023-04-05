# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:29 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def total_travel_time(df):
    return df['Trip Duration'].sum()

def average_travel_time(df):
    return df['Trip Duration'].mean()
