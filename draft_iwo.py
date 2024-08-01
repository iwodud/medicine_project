# To jest mój brudnopis jak co
from icecream import ic
import json
from typing import List
from src.medicine.medicine import Medicine
import datetime as dt


def import_from_file(file_name='data.json'):
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError):
        print(f'File "{file_name}" doesn\'t exist')
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON in file "{file_name}": {e}')
    return {}

def to_date_type(medicine: str) -> dt.date:
    """changes string containing date (year-month-day format) to datetime.date type. doesn't change type permantently."""
    if not isinstance(medicine, str):
        raise TypeError('medicine must be a string')
    date = dt.datetime.strptime(medicine, "%Y-%m-%d").date()
    return date

a = "2024-07-31"
print(type(a))
print(type(to_date_type(a)))
print(type(a))
 

"""
wzięte z githuba, może się przydać:

def get_days_since_date(self, string, date_format):
        if string == None:
            return 999
        datetime_object = datetime.datetime.strptime(string, date_format)
        days = (datetime.date.today() - datetime_object.date()).days
        return days
"""
