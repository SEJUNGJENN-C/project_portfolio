import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    '''Ask for city input from users for interactive experience'''

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower() # Add .lower() to implement error handling so it does not throw any errors due to invalid inputs
        if city in cities:
            break
        else: 
            print('Invalid input!\n')
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("\nWhich month would you like to filter by?\nType 'all' if you don't want to filter by month.\n").lower()
        if month in months:
            break
        else:
            print('Invalid input\n')
    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']
        day = input("Which day would you like to see data for?\n").lower()
        if day in days:
            break
        else: 
            print("Invalid input\n")
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    '''Ask for month and day inputs from users for interactive experience'''
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month) +1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics upon request by user on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    comm_mth = df['month'].mode()[0]
    print('Most common month: {}'.format(comm_mth))

    # TO DO: display the most common day of week
    comm_dow = df['day_of_week'].mode()[0]
    print('Most common day of week: {}'.format(comm_dow))
    
    # TO DO: display the most common start hour
    comm_hour = df['hour'].mode()[0]
    print('Most common start hour: {}'.format(comm_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_start = df['Start Station'].mode()[0] 
    print("The most commonly used start station: {}".format(comm_start))
    
    # TO DO: display most commonly used end station
    comm_end = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(comm_end))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most popular trip from start to end is {}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(str(datetime.timedelta(seconds = total_time))))
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average travel time: {}'.format(str(datetime.timedelta(seconds= mean_time))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print("\nThe counts grouped by users' gender is: {}".format(gender_count))
    else: 
        print ("There is not gender data for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_bday = df['Birth Year'].min()
        recent_bday = df['Birth Year'].max()
        comm_bday = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: {}, Most recent year of birth: {}, Most common year of birth: {}\n".format(earliest_bday, recent_bday, comm_bday))
    else: 
        print("\nThere is no birth data for this city. Please enter Chicago or New York City, instead.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        '''Prompt the user whether they would like want to see the raw data. Return 5 rows of the data at a time if the user's answer is yes 
        and continue until the user input no'''
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_iloc = 0
        while view_data == 'yes': 
            print(df.iloc[0:5])
            start_iloc +=5
            view_display = input("\nDo you wish to continue? Enter yes or no:\n").lower()
            if view_display != 'yes':
                break
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()