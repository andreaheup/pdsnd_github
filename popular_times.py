# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:29 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def popular_times(df):
    """
    analyses in a given dataframe with certain column structure most common trip month/day of week/ start hour
    
    Returns:
        a tuple with 3 entries (most common month, day, hour)
    """
        # Extract hour from the Start Time column to create an hour column 
    df['start_hour'] = df['Start Time'].dt.hour
    # Return most common entries in relevant columns
    return (df.mode()['trip_month'][0], df.mode()['trip_day_of_week'][0], int(df.mode()['start_hour'][0]))
    
