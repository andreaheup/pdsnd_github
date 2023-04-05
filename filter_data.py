# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:43:05 2022

@author: Heup.Andrea
"""

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

# load data file into a dataframe

CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 
             'washington': 'washington.csv'}

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if 
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no 
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply no 
        day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['trip_month'] = df['Start Time'].dt.month
    df['trip_day_of_week'] = df['Start Time'].dt.weekday_name
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        df = df[df['trip_month']==month]
        
    # filter by day of week if applicable
    if day != 'all':       
        # filter by day to create the new dataframe
        df = df[df['trip_day_of_week']==day.title()]
        
    return df





