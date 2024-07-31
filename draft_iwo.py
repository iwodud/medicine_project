# To jest mój brudnopis jak co
from icecream import ic
import json
from typing import List
from src.medicine.medicine import Medicine


def export_to_file(data, file_name='instances.json'):
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    if not isinstance(data, dict):
        raise ValueError('data must be a dictionary')
    with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f'Data successfully exported to "{file_name}".')


# ogólnie ten plik jsonowy działa tak, że jest to słownik instancji, gdzie kluczem jest nazwa leku, a wartością słownik z innymi parametrami leku