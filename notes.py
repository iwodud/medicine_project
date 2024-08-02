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

# rzeczy potrzebne do obliczenia ilości pozostałych dni, ilości pozostałych tabletek, daty kiedy tabletki się wyczerpią: 
# data utworzenia instancji leku, ilość mg leku w tablietce, pozostałą ilość mg leku