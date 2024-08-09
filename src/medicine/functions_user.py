from functions_files import import_from_file, export_to_file
from functions_time import when_will_medicine_run_out


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
    instances_dict[medicine_name]['amount_of_mg'] += amount_of_pills * instances_dict[medicine_name]['mg_per_pill']
    export_to_file(instances_dict)


def remove_medicine_from_dict(dict_name, medicine_name):
        """Removes given key (medicine_name) from given dictionary (dict_name). Returns None"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be a dictionary'
        try:
            del dict_name[medicine_name]
            return True
        except KeyError:
            print(f'Key "{medicine_name}" was not found in dictionary')
            return False


def remove_medicine_from_file(key: str, file_name='data.json'):
    """Removes chosen medicine basing on name (key) from dictionary in file. By default, it removes medicine from data.json"""
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    instances_dict = import_from_file()
    successfull = remove_medicine_from_dict(instances_dict, key)
    if successfull:
        export_to_file(instances_dict)


def check_single_information(medicine):
    data = when_will_medicine_run_out(medicine)
    print(f"""{medicine}
days left: {data[1]} 
finish date: {data[0]}
""")


def check_information():
    data = import_from_file()
    for medicine in data:
        check_single_information(medicine)


def change_daily_dose():
    pass


def create_medicine():
    pass


add_pills('paracetamol_750', 50)
check_information()