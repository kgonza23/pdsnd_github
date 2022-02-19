# I used https://pandas.pydata.org/ and https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf as resources to submit this project

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june", "all"]
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while True:
        city = input('Please enter a city: "chicago, new york city, washington"').lower()
        print(city)
        if city in cities:
            break
        else :
            print ('Hmmm, something isnt quite right. Please enter a valid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter all months or just one month from january to june').lower()
        print(month)
        if month in months :
            break
        else :
            print ('Hmmm, something isnt quite right. Please enter a different month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter day of the week or type all for all the days").lower()
        print(day)
        if day in days_of_week :
            break
        else :
            print('Hmmm, something isnt quite right. Please enter a different day')
    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) # to convert the time to data
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
   #month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df =df[df['month'] == month]
    if day != 'all':
        df =df[df['day_of_week'] == day.title()]
    return df
def time_stats(df,month):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if df['month'].to_string() != month:
        popular_month = df['month'].mode()[0]
        print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Weekday:', popular_day)

    # TO DO: display the most common start hour
# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
# find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
#check this works
    Station_Combinations = (df['Start Station']+ ','+df['End Station']).mode()[0]
    print('Most Common Trip:', Station_Combinations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel = df['Trip Duration'].sum()
    print('Total Travel Time in Seconds:', Total_Travel)

    # TO DO: display mean travel time
    Average_Time = df['Trip Duration'].mean()
    print('Average Travel Time in Seconds:', Average_Time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n Count of Gender \n',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
# find the earliest birth year
    if 'Birth day' in df:
        earliest_year =int(df['Birth day'].min())
        print('\n Earliest Birth Year :\n ',earliest_year)

# find the most recent birth year
    if 'Birth day' in df:
        recent_year = int(df['Birth day'].max())
        print('\n Recent Birth Year :\n ', recent_year)

# find the most common birth year
    if 'Birth day' in df:
        common_birth_year = int(df['Birth day'].mode()[0])
        print('Most Common Birth Year:', common_birth_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw = input("Would you like to see the first 5 rows of raw data? Type 'yes' or 'no'.\n").lower()
        pd.set_option('display.max_columns', 200)
        while True:
          if raw == 'no':
            break
          print(df[i:i+5])
          raw = input("Would you like to see the next 5 rows of raw data?\n").lower()
          i +=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
# Making change 1 to file 
