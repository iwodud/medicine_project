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