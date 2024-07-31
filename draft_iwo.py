# To jest mój brudnopis jak co
from icecream import ic
import json

with open('instances.json', encoding='UTF-8') as f:
    data = json.load(f)
    
print(data['aspiryna_100'])



# ogólnie ten plik jsonowy działa tak, że jest to słownik instancji, gdzie kluczem jest nazwa leku, a wartością słownik z innymi parametrami leku