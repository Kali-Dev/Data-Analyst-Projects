# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:28:33 2018

@author: kalip
"""
import pandas as pd 

#Getting the city name
cities = ['chicago', 'new_york_city', 'washington']
daynames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
monthnames = ['January', 'February', 'March', 'April', 'May', 'June', 'all']
#raw_data = []
#to get the city name, so we can open the csv file accordingly
while True:
    try:
        city = input('Hi! Please enter, which city data you want to analyse: chicago, new_york_city, washington: ')
        city = city.lower()
        print('')
        if city in cities:
            break
        else:
            raise ValueError
    except:
        print('please input valid city name from the given city names')

#getting which filters to be applied
while True:
    try:
        filters_to_be_applied = input('which filter would you like to be applied: month, day, both, or type "none" for no filters to be applied: ')
        filters_to_be_applied = filters_to_be_applied.lower()
        filtersname = ['month', 'day', 'both', 'none']
        if filters_to_be_applied in filtersname:
            break
        else:
            raise ValueError
    except:
        print('please input currect filters as given in the sentence')
#getting month and day names if opted

if filters_to_be_applied == 'month':
    while True:
        try:
            month = input('which month, January, February, March, April, May, June: ')
            month = month.title()
            day = 'All'
            if month in monthnames:
                break
            else:
                raise ValueError
        except:
            print('please print currect month as given in the sentence')
            
elif filters_to_be_applied == 'day':
    while True:
        try:
            day = input('which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday: ')
            day = day.title()
            month = 'All'
            if day in daynames:
                break
            else:
                raise ValueError
        except:
            print('This is not a valid day, Please enter valid weekdayname as given in the sentence')
        
elif filters_to_be_applied == 'both':
    while True:
        try:
            month = input('which month, January, February, March, April, May, June: ')
            day = input('which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday: ')
            month = month.title()
            day = day.title()
            if (month in monthnames) & (day in daynames):
                break
            else:
                raise ValueError
        except:
            print('entered wrong month or day name, please enter as in the sentences')

else:
    month = 'All'
    day = 'All'
print('calculating statastics')
print('')
def statcalculator(city,month,day):
    '''to return the nice stats table by applying the required filters, opted by the user
    city = city data which the user want to see, like chicago, washington etc
    month = function calculates the stats by applying monthly filters, like january, february etc
    day = function calculates the stats by applying day filters, like monday, tuesday etc
    '''
    
    filenames = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    global df
    df = pd.read_csv(filenames[city])
    
    #converting to datetime format so that the calcuation will be easy
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Hour'] = df['Start Time'].dt.hour
    df['Day'] = df['Start Time'].dt.day
    df['Week day'] = df['Start Time'].dt.weekday_name
    
    #applying filters on the data frame, which are opted by the user
    
    if filters_to_be_applied == 'month':
        monthvalue = monthnames.index(month) + 1
        df = df[df['Month'] == monthvalue]
    elif filters_to_be_applied == 'day':
        df = df[df['Week day'] == day]
    elif filters_to_be_applied == 'both':
        monthvalue = monthnames.index(month) + 1
        df = df[(df['Month'] == monthvalue) & (df['Week day'] == day)]
    else:
        pass
    
    # calculating stats on the filtered data frame    
    popular_weekday = df['Week day'].mode()[0]
    popular_hour = df['Hour'].mode()[0]
    popular_month = df['Month'].mode()[0]
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    user_types = df['User Type'].value_counts()
    total_subscribers = user_types[0]
    total_customers = user_types[1]
    
    #final dictionary of stats that will be seen by the end user
    highest_business =  {'busiest day:':pd.Series(popular_weekday),
            'busiest hour:': pd.Series(popular_hour),
            'busiest month': pd.Series(popular_month),
            'Most Popular Start Station': pd.Series(popular_start_station),
            'Most Popular End Station': pd.Series(popular_end_station),
            'Total_subscribers': total_subscribers,
            'Total_customers': total_customers}
    
    final_df = pd.DataFrame(highest_business)
    return ((final_df)) 
op = statcalculator(city,month,day)
print(op)

while True:
    try:
        raw_data = input('Do you want to see the raw data that is used for the calculation, type yes or no: ')
        raw_data = raw_data.lower()
        if (raw_data == 'yes') or (raw_data == 'no'):
            break
        else:
            raise ValueError
    except:
        print('typo! please enter either yes or no')
if raw_data == 'yes':
    print(df)
else:
    print('thanks! hope you find the stats calculator useful')
    
    