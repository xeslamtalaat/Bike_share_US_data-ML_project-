import time
import pandas as pd
import numpy as np

#define code for each stat to load csv file
CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
#1st function to define inputs by user to filter data
    print('Hello! Let\'s explore some US bikeshare data!')
    #ask to input city code
    city = input("\n please enter the city as below:\n ch for chicago \n ny for new york city \n w for washington \n").lower()
    while city not in CITY_DATA.keys():
        print("\n try again with right city")
        city = input("\n please chose the city from below:\n ch for chicago \n ny for new york \n w for washington \n").lower()
    #ask to input month to filter data by month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('\n please chose month from the below: \n january \n february \n march \n april \n may \n june \n all \n').lower()
    while month not in months:
        print('wrong month try again!!')
        month = input('\n please chose month from the below: \n january \n february \n march \n april \n may \n june \n').lower()
    #ask to input the dat to filter data by day
    week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sunday']
    day = input("\n please chose day (type all to chose whole weekdays): \n").lower()
    while day not in week:
        print('\n wrong day please enter again!!')
        day = input("\n please chose day (type all to chose whole weekdays): \n").lower()


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
#2nd function to load the dataframe and filter data by inputs on the preiviews function
    #load data frame
    df = pd.read_csv(CITY_DATA[city])
    #swtich the start time col. to datetime format to extract more data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #creat new col. for month
    df['month'] = df['Start Time'].dt.month_name()
    #creat new col. for day
    df['start day'] = df['Start Time'].dt.day_name()
    #create new col. for hour
    df['start hour'] = df['Start Time'].dt.hour
    #filter the dataframe by month
    if month != "all":
        df = df[df["month"] == month.title()]
    #filter the dataframe by day
    if day != "all":
        df = df[df['start day'] == day.title()]

    return df

def time_stats(df):
#3rd function to calculate time stats from dataframe created on the 2nd function
    print('\nCalculating The Most Frequent Times of Travel...\n')

    #find most common month
    popular_month = df['month'].mode()[0]
    print("Most Frequent month: " + popular_month)

    #find most common day of week
    popular_day = df['start day'].mode()[0]
    print("Most Frequent day: " + popular_day)

    #find most common start hour
    popular_hour = df['start hour'].mode()[0]
    print("Most Frequent hour: " + str(popular_hour))


    print('-'*40)

def station_stats(df):
#4th function to calculate stats about stations using the dataframe created on 2nd function
    print('\nCalculating The Most Popular Stations and Trip...\n')
    #find the most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print("Most Popular Start Station: " + most_start)

    #find the most commonly used end station
    most_end = df['End Station'].mode()[0]
    print("Most Popular End Station: " + most_end)

    #creat new col. to create the trip route
    df['route'] = 'from  ' + df['Start Station'] + '  to  ' + df['End Station']
    #find the most common route
    print("Most Frequent Route: " + df['route'].mode()[0])

    print('-'*40)

def trip_duration_stats(df):
#5th function to calculate stats about trip duration using the dataframe created on 2nd function
    print('\nCalculating Trip Duration...\n')
    #switch the end time col to datetime type to made calcualatiom (start time col switched before on previous function)
    df['End Time'] = pd.to_datetime(df['End Time'])
    #crate trip time col to calculate trip duration
    df['trip_time'] = df['End Time'] - df['Start Time']
    #calculate the total trips duration
    total = df['trip_time'].sum()
    print("Total travel time: " + str(total))

    #calculate the average trip duration
    mean = df['trip_time'].mean()
    print("Average travel time: " + str(mean))


    print('-'*40)

def user_stats(df):
#6th function to show informations about users on dataframe created on the 2nd function
    print('\nCalculating User Stats...\n')

    #counts the different user types
    users_types = df['User Type'].value_counts()
    print('Users Types Count: \n' +  str(users_types))

    #counts the genders but using loop because this data not available on all stats
    if "Gender" in df :
        gender_count = df['Gender'].value_counts()
        print('Users Gender Count: \n' + str(gender_count))
    else:
        print("No gender data on this state")
    #stats of the birth year but using loop because this data not available on all stats
    if 'Birth Year' in df:
        earliest = df['Birth Year'].max()
        print('Recent Birth Year: \n' + str(earliest))
        recent = df['Birth Year'].min()
        print('Earliest Birth Year: \n' + str(recent))
        common = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: \n' + str(common))
    else:
        print("No birth year data on this state")



    print('-'*40)

def display_raw_data(df):
#7th function to ask user if he want to show 5 rows from dataframe to check it
    print('\nRaw data is available to check... \n')
    #using many loops to give user options to show dataframe 5 rows by 5 rows if he need it
    loc = 0
    while True:
        raw = input('To View the raw data in 5 rows please type: Yes \n').lower()
        if raw not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif raw == 'yes':
            print(df.iloc[loc:loc+5])
            loc += 5


        elif raw == 'no':
            print('\nExiting...')
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
