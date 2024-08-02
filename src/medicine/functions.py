"""This file contains functions used outside of classes"""

import json
import datetime as dt
from medicine import Medicine


def import_from_file(file_name='data.json'):
    """imports whole file"""
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

# rzeczy potrzebne do obliczenia ilości pozostałych dni, ilości pozostałych tabletek, daty kiedy tabletki się wyczerpią: 
# data utworzenia instancji leku, ilość mg leku w tablietce, pozostałą ilość mg leku

def give_list_of_wanted_medicines(medicine_name: str, file='data.json') -> list[str]:
    """returns list of medicine_names from data base matching given name (medicine_name). if you type in 'aspiryna' or 'aspiryna_100_ you get ['aspiryna_100'].
    if you type in 'paracetamol' you get ['paracetamol_500', 'paracetamol_750'], but if you type in 'paracetamol_500', you get ['paracetamol_500']."""
    if not isinstance(medicine_name, str):
        raise TypeError("'medicine_name' must be a string")
    list_of_results = []
    data_base = import_from_file('data.json')
    for medicine in data_base:
        if isolate_name(medicine) == medicine_name or medicine == medicine_name:
            list_of_results.append(medicine)
    if list_of_results == []:
        raise KeyError(f"{medicine_name} wasn't found in data base")
    print(list_of_results)
    return list_of_results

give_list_of_wanted_medicines('d')
