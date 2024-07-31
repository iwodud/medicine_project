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
        
def how_much_in_mg(*medicines: Medicine):
    """Takes medicine's names (STR) and returns amount of the medicine in milligrams"""
    sum_of_mg = []  # to this list I add milligrams multiplied by the number of pills
    for medicine in medicines:
        assert isinstance(medicine, Medicine), 'medicines is supposed to be medicine.Medicine'
        amount_of_pills = medicine.current_amount
        mg_per_pill = medicine.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        sum_of_mg.append(amount_of_mg)
    return sum(sum_of_mg)