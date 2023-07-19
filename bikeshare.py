import time
import pandas as pd
import numpy as np
basepath = "C:\\Users\\laura\\udacity\\Test\\"
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

    while True:
        city = input('Would you like to see the data for Chicago, New York City, or Washington? Please enter one these cities: ')
        city = city.lower()
        
        if city not in CITY_DATA:
            print('YOu choose a wrong city.')
            continue
        break

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True:
        month = input('Which month would you like to see? Please enter the month January, February, March, April, May or June (- other months are not available yet): ')
        month = month.lower()
       
        if month not in months:
            print('You choose the wrong month.')
            continue
        break
    month = months.index(month)+1

    df = df[ df['month'] == month ]
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Please enter the day you would like to see the data from (monday, tuesday, wednesday etc.): ')
        day = day.lower()

        if day not in days:
            print('You choose a wrong day.')
            continue
        break
    day = days.index(day)+1
    df = df[ df['day_of_week'] == day ]

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['month name'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.dayofweek +1
    df['day name'] = df['Start Time'].dt.day_name()

    # filter for month
    if(month != 'all'):
        df = df[df['month'] == month]

    # filter for df
    if (day != 'all'):
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_com_month = df['month'].mode()
    print('The most common month is ' + most_com_month.to_string(index=False) + '.')

    # display the most common day of week
    most_com_day = df['day'].mode()
    print('The most common weekday is ' + most_com_day.to_string(index=False) + '.')

    # display the most common start hour
    most_com_start_hour = df['Start Time'].dt.hour.mode()
    print('The most common hour is ' + most_com_start_hour.to_string(index=False) + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()

    print(f'The most commonly used start station is {most_used_start_station[0]}.')

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()
    print(f'The most commonly used end station is {most_used_end_station.to_string(index=False)}.')

    # display most frequent combination of start station and end station trip/ muss aus String eine Liste aus Strings machen um die zusammenzufügen, daher zwei eckige KLammern
    most_com_comb = df[['Start Station', 'End Station']].mode()
    print(f"The most frequent used start and end station combination is {most_com_comb['Start Station'][0]} and {most_com_comb['End Station'][0]}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time / Nummern formatieren: https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is {total_travel_time/60 :.2f} minutes.")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is {mean_travel_time/60 :.2f} minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    counts_of_user_types = df.groupby("User Type")["User Type"].count()
    print(counts_of_user_types)

    #Display counts of gender
    if "Gender" in df:
        counts_of_gender = df.groupby("Gender")["Gender"].count()
        print(counts_of_gender)

    #Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        most_recent_birth_year = df["Birth Year"].max()
        print(f"The most recent year of birth is {most_recent_birth_year}.")
        
        most_common_birth_year = df["Birth Year"].mode()
        print(f'The most common year of birth is {most_common_birth_year.to_string(index=False)}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def row(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    x = 0
    while view_data == 'yes':
        print(df.iloc[x: x+5])
        x += 5
        view_data = input("Do you wish to see the next 5 rows? Please enter yes or no: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
             break


if __name__ == "__main__":
	main()
