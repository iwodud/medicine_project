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
