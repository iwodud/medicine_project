# Oliwia, jak to czytasz to nie przejmuj się tym plikiem ani plikiem setup.py
import calendar
import datetime

# import datemath

# might be useful
# print(calendar.monthcalendar(2024, 5))
# print(calendar.monthrange(2024, 5))
# today = datetime.date.today()
# delta = datetime.timedelta(days=31)

today = datetime.date.today()
delta = datetime.timedelta(days=31)

today = datetime.date.today()
delta = datetime.timedelta(days=7)
print(today + delta)

# print(today + delta)

birthday = datetime.date(2024, 5, 29)

till_bday = birthday - today
print(till_bday)
