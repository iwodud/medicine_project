import json


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

