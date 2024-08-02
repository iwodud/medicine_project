"""This file contains functions used outside of classes"""

import datetime as dt
import json

from medicine import Medicine



def import_from_file(file_name='data.json'):
    """imports whole file"""
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    
    except FileNotFoundError:
        print(f'File "{file_name}" doesn\'t exist')
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON in file "{file_name}": {e}')
    return {}


def export_to_file(data, file_name='data.json'):
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    if not isinstance(data, dict):
        raise ValueError('data must be a dictionary')
    
    with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f'data successfully updated in "{file_name}"')


def remove_instance_from_file(key, file_name='data.json'):
    """Removes chosen medicine basing on name (key) from dictionary in file. By default it removes itself from data.json"""
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    def remove_medicine_from_dict(dict_name, key):
        """Removes given key (key) from given dictionary (dict_name). Returns None"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be a DICT'
        try:
            del dict_name[key]
        except KeyError:
            print(f'Key "{key}" was not found in dictionary')
    
    instances_dict = import_from_file()
    remove_medicine_from_dict(instances_dict, key)
    export_to_file(instances_dict)


def add_pills(medicine_name: str, amount_of_pills: int, file_name='data.json'):
    """Adds more pills to chosen medicine in file (you use when you bought new package for example)"""
    if not isinstance(medicine_name, str):
        raise TypeError('medicine_name must be a string')
    if not isinstance(amount_of_pills, int):
        raise TypeError('amount_of_pills must be an integer')
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    instances_dict = import_from_file()
    instances_dict[medicine_name]['amount_of_pills'] += amount_of_pills
    export_to_file(instances_dict)


def to_date_type(medicine: str) -> dt.date:
    """changes string containing date (year-month-day format) to datetime.date type. doesn't change type permantently."""
    if not isinstance(medicine, str):
        raise TypeError('medicine must be a string')
    try:
        date = dt.datetime.strptime(medicine, "%Y-%m-%d").date()
        return date
    except ValueError:
        raise ValueError("The date string must be in 'YYYY-MM-DD' format and represent a valid date.")


def isolate_name(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("'string' must be a string")
    
    name = string.split('_')[0]
    return name 


def get_list_of_wanted_medicines(medicine_name: str, file_name='data.json') -> list[str]:
    """returns list of medicine_names from data base matching given name (medicine_name). if you type in 'aspiryna' or 'aspiryna_100_ you get ['aspiryna_100'].
    if you type in 'paracetamol' you get ['paracetamol_500', 'paracetamol_750'], but if you type in 'paracetamol_500', you get ['paracetamol_500']."""
    if not isinstance(medicine_name, str):
        raise TypeError("'medicine_name' must be a string")
    
    list_of_results = []
    database = import_from_file(file_name)
    
    for medicine in database:
        if isolate_name(medicine) == medicine_name or medicine == medicine_name:
            list_of_results.append(medicine)
    
    if list_of_results == []:
        raise KeyError(f"{medicine_name} wasn't found in database")
    
    return list_of_results


def import_selected_medicine(medicine_name: str, file_name='data.json') -> list[dict]:
    """basing on given medicine name, the function returns list of all matching medicines dictionarys from database."""
    if not isinstance(medicine_name, str):
        raise TypeError("'medicine_name' must be a string")
    
    list_of_medicines = []
    database = import_from_file(file_name)
    list_of_keys = get_list_of_wanted_medicines(medicine_name)
    
    for key in list_of_keys:
        list_of_medicines.append(database[key])
    
    return(list_of_medicines)


def how_many_days_passed(given_date: str) -> int:
    if not isinstance(given_date, str):
        raise TypeError('given_date must be a string')

    current_date = dt.datetime.now().date()
    days_passed = current_date - to_date_type(given_date)
    return days_passed.days


def days_to_amount_of_medicine(number_of_days: int, daily_dose_in_mg: int):
    if not (isinstance(number_of_days, int) and isinstance(daily_dose_in_mg, int)):
        raise TypeError('arguments must be integers')
    if number_of_days <= 0 or daily_dose_in_mg <= 0:
        raise ValueError('arguments must be greater than zero')
    
    return number_of_days * daily_dose_in_mg