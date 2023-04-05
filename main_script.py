# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:26:32 2022

@author: Heup.Andrea
"""
import pandas as pd
import filter_data as fd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

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


months = ['January', 'February', 'March', 'April', 'May', 'June']

df = fd.load_data(city,month,day)

# #1 Popular times of travel

# Extract hour from the Start Time column to create an hour column
df['start_hour'] = df['Start Time'].dt.hour
# Find most common trip month
popular_month = df.mode()['trip_month'][0] 
# Find the most common hour (from 0 to 23)
popular_hour = int(df.mode()['start_hour'][0])
# Find the most common weekday 
popular_weekday = df.mode()['trip_day_of_week'][0]

# Print result 
print('\n\nHere comes the statistics for bike rentals in {}, filtered by months {} and weekday {}.'.format(city.title(),month.title(), day.title()))

print('\n#1 Popular times of travel')
print('\nMost popular rental month: {}'.format(months[int(popular_month-1)]))
print('Most popular rental day: {}'.format(popular_weekday))
print('Most popular start rental hour: {} h'.format(popular_hour))


#2 Popular stations and trip

# Find most common start station
popular_start_station = df.mode()['Start Station'][0]
# Find most common end station
popular_end_station = df.mode()['End Station'][0]

# Print result 
print('\n#2 Popular stations and trip')
print('\nMost popular start station: {}'.format(popular_start_station))
print('Most popular end station: {}'.format(popular_end_station))

# Find most frequent combination of start station and end station
# Create dataframe groupby
x = df.groupby(['Start Station', 'End Station'])

# Find max value index in size of each groupby groups
popular_comb = x.size().idxmax()

# Find size of max combination
popular_comb_count = x.size()[popular_comb]

# Print result
print('Most popular combination of start-end stations: {} and {}. It occured {} times.'.format(popular_comb[0], popular_comb[1], popular_comb_count,))



#3 Trip duration

total_travel_duration = df['Trip Duration'].sum()
average_travel_time = df['Trip Duration'].mean()

# Print result
print('\n#3 Trip duration')
print('\nTotal trip duration: {} seconds'.format('{:,}'.format(total_travel_duration)))
print('Average trip duration: {} seconds'.format('{:,}'.format(average_travel_time)))




#4 User info

value_list = df['User Type'].dropna().unique()
print('\n#4 User info')
print('\nUser types and counts:')
for i in value_list:
    print(i+' - {}'.format('{:,}'.format(df['User Type'].value_counts()[i])))
    
if city.lower() != 'washington':
    y = df.groupby('Gender').size()
    print('\nUser genders:')
    for i in range(len(y)):
        print(str(y.index[i])+' - '+ str('{:,}'.format(y[i])))
    
    earliest_by = int(df['Birth Year'].min())
    recent_by = int(df['Birth Year'].max())
    most_common_by = int(df.mode()['Birth Year'][0])
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
   print(df.iloc[6*(i-1):6*i-1])
   # Entered Y/N anwer by user is checked and is forced to be re-entered in case of mistakes.
   while valid == True:
       raw_data = input("Would you like to see 5 more rows? Enter Y/N \n")
       valid = raw_data.lower() not in {'y','n'}
       if valid == True:
           print("\nOooops!!! There seems to be a mistake. Please try again.")