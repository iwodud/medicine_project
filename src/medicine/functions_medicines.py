from functions_files import import_from_file, export_to_file


def isolate_name(string: str) -> str:
    """isolates name of medicine from it's instance's name (for example apap from apap_500)"""
    if not isinstance(string, str):
        raise TypeError("'string' must be a string")
    
    name = string.split('_')[0]
    return name 


def get_names_of_wanted_medicines(medicine_name: str, file_name='data.json') -> list[str]:
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


def get_selected_medicine(medicine_name: str, file_name='data.json') -> list[dict]:
    """basing on given medicine name, the function returns list of all matching medicines dictionarys from database."""
    if not isinstance(medicine_name, str):
        raise TypeError("'medicine_name' must be a string")
    
    list_of_medicines = []
    database = import_from_file(file_name)
    list_of_keys = get_names_of_wanted_medicines(medicine_name)
    
    for key in list_of_keys:
        list_of_medicines.append(database[key])
    
    return(list_of_medicines)