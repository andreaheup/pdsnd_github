# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:29 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def user_type_counts(df):
    value_list = df['User Type'].dropna().unique()
    dict = {}
    for i in value_list:
        dict[i] = df['User Type'].value_counts()[i]
    return dict

def gender_counts(df):
    y = df.groupby('Gender').size()
    dict = {}
    for i in range(len(y)):
        dict[y.index[i]] = y[i]
    return dict
    
def earliest_by (df): 
    return int(df['Birth Year'].min())

def recent_by (df):
    return int(df['Birth Year'].max())
    
def most_common_by (df):
   return int(df.mode()['Birth Year'][0])