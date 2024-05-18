from icecream import ic
from medicine_classes import Medicine
import pickle


def save_dict_to_file(dictionary, file_name):
    assert isinstance(dictionary, dict), 'dictionary is supposed to be DICT'
    assert isinstance(file_name, str), 'file_name is supposed to be STR'
    import pickle  # służy do zapisywania binarnego plików
    with open(file_name, 'wb') as file:  # tryb wb też
        pickle.dump(dictionary, file)  # żeby słownik zapisywać do pliku


def how_much_in_mg(*medicines):
    """Takes medicine's names (STR) and returns amount of the medicine in milligrams"""
    sum_of_mg = []  # to this list I add milligrams multiplied by the number of pills
    for medicine in medicines:
        assert isinstance(medicine, Medicine), 'medicines is supposed to be medicine_classes.Medicine'
        amount_of_pills = medicine.current_amount
        mg_per_pill = medicine.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        sum_of_mg.append(amount_of_mg)
    return sum(sum_of_mg)

def read_pickle_file(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)
lacosamide_100 = Medicine('lacosamide', 100, 200, 50)


# ic(Medicine.instances)
data = read_pickle_file('instances.p')
neurotop_600.remove_instance_from_file()
ic(read_pickle_file('instances.p'))

print(data['lacosamide_100'][1])