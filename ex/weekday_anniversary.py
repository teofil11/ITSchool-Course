from datetime import datetime

def anniversary(n):
    birth_day = input('Your birth day(year/month/day): ')
    year = int(birth_day.split('/')[0])
    month = int(birth_day.split('/')[1])
    day = int(birth_day.split('/')[2])
    year_now = datetime.now().year
    n_year = year_now + n
    print(datetime(n_year,month,day).strftime('%A'))
