# To jest mój brudnopis jak co
from icecream import ic
from src.medicine.medicine import Medicine


example_dict = {
    1: "Aspirin",
    2: "Paracetamol",
    3: "Ibuprofen",
    4: "Amoxicillin",
    5: "Ciprofloxacin"
}

ic(example_dict)
ic(example_dict)



# ogólnie ten plik jsonowy działa tak, że jest to słownik instancji, gdzie kluczem jest nazwa leku, a wartością słownik z innymi parametrami leku