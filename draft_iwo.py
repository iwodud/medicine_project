from medicine_classes import Medicine
import datetime as dt

vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)

def how_many_days_to(start_day, end_day):
    start_day = dt.date.today()


today = dt.date.today()
delta = dt.timedelta(days=7)
print(today + delta)

def add(a, b):
    return a + b