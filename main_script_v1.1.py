# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:26:32 2022

@author: Heup.Andrea
"""
import pandas as pd
import filter_data as fd
import popular_times as pt
import popular_stations as ps
import travel_time_stats as tts
import user_info as ui
import raw_data_view as rdv

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

restart = 'y'
while restart == 'y':
    # Introducing a control variable in case of wrong entries by user
    valid = True
    
    # Entered city name by user is checked and is forced to be re-entered in case of mistakes.
    while valid == True:
        city = input("Would you like to see data for Chicago, New York or Washington? \nPlease enter the desired cityname: \n")
        valid = city.lower() not in {'chicago', 'new york','washington'}
        if valid == True:
            print("\nOooops!!! There seems to be a mistake. Please try again.")
    
    # Control variable will be used in coding blocks below and is reset to True
    valid = True
    
    # Entered date filter by user is checked and is forced to be re-entered in case of mistakes
    while valid == True:
        date_filter = input("Would you like to filter the data by month, day or not at all? \nPlease enter month, day or none: \n")
        valid = date_filter.lower() not in {'month', 'day', 'none'}
        if valid == True:
            print("\nOooops!!! There seems to be a mistake. Please try again.")
    
    # Control variable will be used in coding blocks below and is reset to True
    valid = True
    
    # Entered month or day filter by user is checked and is forced to be re-entered in case of mistakes
    while valid == True:
        if date_filter.lower() == 'month':
            while valid == True:
                month = input("Which month would you like to look at? \nPlease enter January, February, March, April, May or June: \n")
                valid = month.lower() not in {'january','february','march','april','may','june'}
                day = 'all'    
                if valid == True:
                     print("\nOooops!!! There seems to be a mistake. Please try again.")
        elif date_filter.lower() == 'day':
            while valid == True:
                day = input("Which day would you like to look at? \nPlease enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday: \n")
                valid = day.lower() not in {'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
                month = 'all'
                if valid == True:
                     print("\nOooops!!! There seems to be a mistake. Please try again.")
        else:
                month ='all'
                day = 'all'
                valid = False             # necessary to prevent endless while loop in case date_filter = 'none'
    
    # Auxilliary lists
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    
    #load and filter chosen file pursuant inputs
    df = fd.load_data(city,month,day)
    
    # Get popular times of travel
    popular_month, popular_weekday, popular_hour = pt.popular_times(df)
    
    # Get popular start/end staations and combinations 
    pop_start, pop_end, pop_start_comb, pop_end_comb, pop_start_end_comb_count = ps.popular_stations(df)
    
    # Get travel time statistics
    total_travel_time = tts.total_travel_time(df)
    average_travel_time = tts.average_travel_time(df)
    
    # Get User Type Counts
    utc = ui.user_type_counts(df)
    
    # Get Gender Counts
    if city.lower() != 'washington':
        gc = ui.gender_counts(df)
    
    # Get infos about birthyears
    if city.lower() != 'washington':
        earliest_by = ui.earliest_by(df)
        recent_by = ui.recent_by(df)
        most_common_by = ui.most_common_by(df)
    
    # Print results 
    print('\n\nHere comes the statistics for bike rentals in {}, filtered by months {} and weekday {}.'.format(city.title(),month.title(), day.title()))
        
    print('\n#1 Popular times of travel')
    print('\nMost popular rental month: {}'.format(months[int(popular_month-1)]))
    print('Most popular rental day: {}'.format(popular_weekday))
    print('Most popular start rental hour: {} h'.format(popular_hour))
    
    print('\n#2 Popular stations and trip')
    print('\nMost popular start station: {}'.format(pop_start))
    print('Most popular end station: {}'.format(pop_end))
    print('Most popular combination of start-end stations: {} and {}. It occured {} times.'.format(pop_start_comb, pop_end_comb, pop_start_end_comb_count))
    
    print('\n#3 Trip duration')
    print('\nTotal trip duration: {} seconds'.format('{:,}'.format(total_travel_time)))
    print('Average trip duration: {} seconds'.format('{:,}'.format(average_travel_time)))
    
    print('\n#4 User info')
    print('\nUser types and counts:')
    
    for i in utc:
        print('{}'.format(i) +' - {:,}'.format(utc[i]))
        
    if city.lower() != 'washington':
        print('\nUser genders:')
        for i in gc:
            print('{}'.format(i)+' - '+ '{:,}'.format(gc[i]))    
        print('Earliest birthyear: {}'.format(earliest_by))
        print('Most recent birthyear: {}'.format(recent_by))
        print('Most common year of birth: {}'.format(most_common_by))
        
    
    # Control variable will be used in coding blocks below and is reset to True     
    valid = True
    
    # Entered Y/N anwer by user is checked and is forced to be re-entered in case of mistakes.
    while valid == True:
        raw_data = input("Would you like to see 5 rows of the underlying raw data according to your chosen filters? Y/N \n")
        valid = raw_data.lower() not in {'y','n'}
        if valid == True:
            print("\nOooops!!! There seems to be a mistake. Please try again.")
    
    # Print for every "Y" entered by the user next 5 rows from the rawdata 
    i=0
    while raw_data.lower()=='y':
       # Control variable will be used in coding blocks below and is reset to True   
       valid = True
       i+=1 
       print(rdv.raw_data_view(df,i))
       # Entered Y/N anwer by user is checked and is forced to be re-entered in case of mistakes.
       while valid == True:
           raw_data = input("Would you like to see 5 more rows? Enter Y/N \n")
           valid = raw_data.lower() not in {'y','n'}
           if valid == True:
               print("\nOooops!!! There seems to be a mistake. Please try again.")
               
    restart = input("Would you like to restart? y/n")