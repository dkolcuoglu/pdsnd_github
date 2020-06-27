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
    while(True): 
        city=input("Please enter a city name ").lower()
        if city =="chicago" or city=="new york city" or city =="washington":
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True): 
        month=input("Please enter a month ").lower()
        if month in ["all", "january", "february","march","april","may","june"]:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True): 
        day=input("Please enter a day ").lower()
        if day in ["all", "monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]:
            break

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
    import pandas as pd 
    if city=="chicago" or city=="washington": 
        df=pd.read_csv(city+".csv",index_col=0)
    elif  city=="new york city":
        df=pd.read_csv(city.replace(" ","_")+".csv",index_col=0)
        
    
    import datetime as dt
    monthdict={"all":-1,"january":1,"february":2,"march":3,"april":4,"may":5,"june":6}
    daydict={"all":-1,"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    if month!="all":
        a=df[pd.to_datetime(df["Start Time"]).dt.month==monthdict[month]]
    else :
        a=df
    if day != "all":
        b=a[pd.to_datetime(a["Start Time"]).dt.weekday==daydict[day]]
    else:
        b=a
    

    return b


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    import time
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    import datetime as dt
    import pandas as pd 
    monthdict={"all":-1,"january":1,"february":2,"march":3,"april":4,"may":5,"june":6}
    daydict={"all":-1,"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month
    def get_key_d(val): 
                for key, value in daydict.items(): 
                     if val == value: 
                        return key 

                return "key doesn't exist"
    print("Most common day is",get_key_d(pd.to_datetime(df["Start Time"]).dt.weekday.value_counts().index[0]))

    def get_key_m(val): 
        for key, value in monthdict.items(): 
             if val == value: 
                return key 

        return "key doesn't exist"
    print("Most common month is",get_key_m(pd.to_datetime(df["Start Time"]).dt.month.value_counts().index[0]))


    print("Most common hour",pd.to_datetime(df["Start Time"]).dt.hour.value_counts().index[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print("Most common Start Station is",df["Start Station"].value_counts().index[0])
    print("Most common End Station is",df["End Station"].value_counts().index[0])
    paths="FROM "+df["Start Station"]+" TO "+ df["End Station"]
    print("Most common route is",paths.value_counts().index[0])
    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    import time 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Average duration is", df["Trip Duration"].mean())
    print("Total duration is",df["Trip Duration"].sum())

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print("Counts of User Types:")
    print(df["User Type"].value_counts())
    print('-'*10)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
        print("Earliest year is ",df["Birth Year"].min())
        print("Most recent year is ",df["Birth Year"].max())
        print("Most common year is ",df["Birth Year"].value_counts().index[0])
    except: 
        print("Birth Year is not available with selected filters !! ")
    print('-'*10)


    # TO DO: Display counts of gender
    try: 
        print("Counts of Genders:")
        print(df["Gender"].value_counts())
    except:
        print("Gender is not available with selected filters!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        start=0
        end=5
        while True : 
            showmore=input('\nWould you like to see 5 row from filtered data? Enter yes or no.\n')
            if showmore.lower()=="yes":
                print(df[start:end])
            elif showmore.lower()=="no":
                break
            else: 
                print("Incorrectly entered input,Please enter yes or no.")
            start=start+5
            end=end+5
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
