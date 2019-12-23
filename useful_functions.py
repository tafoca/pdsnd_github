ITY_DATA = { 'chicago': 'chicago.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    CITY_NAMES = ['chicago','new york city','washington']

    city = (input("Please enter the city name only amoung the names: [chicago,new york city,washington]\n")).lower()
    while city not in  CITY_NAMES:
        print()
        city = (input("Please enter the city name only amoung the names: [chicago,new york city,washington]\n")).lower()
   
    # get user input for month (all, january, february, ... , june)
    MONTH_NAMES = ['all','january','february','march','april','may','june']

    month_name = (input("Please enter valid month in interval of [january - june] or all :\n")).lower()
    while month_name not in  MONTH_NAMES:
        print()
        month_name = (input("Please enter valid month in interval of [january - june] or all : \n")).lower()
   

    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_NAMES = ['all','monday','tuesday','wenesday','thursday','friday','saturday','sunday']

    day_name = (input("Please enter valid day in interval of [monday - sunday] or all :\n")).lower()
    while day_name not in DAY_NAMES:
        print()
        day_name = (input("Please enter valid day in interval of [monday - sunday] or all : \n")).lower()

    print('-'*40)
    return city, month_name, day_name




def main():
    print("Testing city enter function")
    print(get_filters()) 
   # assert(mean(n_list) == correct_mean)
    print("All tests passed!")
#indicate this execution it possible only on this file not in the file that import this module
if __name__ == '__main__':
    main()