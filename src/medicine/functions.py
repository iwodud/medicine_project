"""This file contains functions used outside of classes"""
import json
from typing import List
from medicine import Medicine

def remove_instance_from_file(key, file_name='instances.json'):
    """Removes instance of Medicine basing on name (key) from dictionary in file. By default it removes itself from instances.json"""
    assert isinstance(file_name, str), 'file_name is supposed to be STR'
    
    def remove_medicine_from_dict(dict_name, key):
        """Removes given key (key) from given dictionary (dict_name). Returns None"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be a DICT'
        try:
            del dict_name[key]
        except KeyError:
            print(f'Key "{key}" was not found in dictionary')
    
    try:
        with open(file_name, 'r') as file:
            instances_dict = json.load(file)
    except (FileNotFoundError, EOFError):
        print(f'File {file_name} doesn\'t exist')
        return None

    remove_medicine_from_dict(instances_dict, key)

    with open(file_name, 'w') as file:
        json.dump(instances_dict, file, indent=4)


def add_pills(medicine_name: str, amount_of_pills: int, file_name='instances.json'):
    """Adds more pills to chosen medicine in file (you use when you bought new package for example)"""
    assert isinstance(amount_of_pills, int), 'amount_of_pills is supposed to be an integer'
    assert isinstance(medicine_name, str), 'medicine_name is supposed to be a string'
    
    try:
        with open(file_name, 'r') as file:
            instances_dict = json.load(file)
    except (FileNotFoundError, EOFError):
        print(f'File {file_name} doesn\'t exist')
        return None
    
    print(instances_dict[medicine_name])
    instances_dict[medicine_name]['amount_of_pills'] += amount_of_pills
    print(instances_dict[medicine_name])
    
    with open(file_name, 'w') as file:
        json.dump(instances_dict, file, indent=4)
        
add_pills('aspiryna_100', 10)