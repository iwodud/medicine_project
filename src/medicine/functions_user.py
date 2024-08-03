from functions_files import import_from_file, export_to_file


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


def remove_medicine_from_file(key, file_name='data.json'):
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


def change_daily_dose():
    pass


def show_medicine():
    pass