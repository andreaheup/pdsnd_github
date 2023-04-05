# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:58:29 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def popular_stations(df):
    """
    analysis in a given dataframe with certain column structure most common start/end stations and most common combination of strat and end station
    
    Returns:
        a tuple with 5 entries (most common start station, end station, start of most common start/end combination, end of most common start/end combination, no of occurences of most common start/end comnbination)
    """
    # Find most frequent combination of start station and end station
    # Create dataframe groupby
    x = df.groupby(['Start Station', 'End Station'])

    # Find max value index in size of each groupby groups
    popular_comb = x.size().idxmax()
    
    # Find size of max combination
    popular_comb_count = x.size()[popular_comb]

    # Find most common start station

    # Find most common end station

    # Return most common entries in relevant columns
    return (df.mode()['Start Station'][0], df.mode()['End Station'][0],popular_comb[0], popular_comb[1], popular_comb_count)
    
