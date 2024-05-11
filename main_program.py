from medicine_classes import Medicine


def save_dict_to_file(dictionary, file_name):
    assert isinstance(dictionary, dict), 'dictionary is supposed to be DICT'
    assert isinstance(file_name, str), 'file_name is supposed to be STR'
    import pickle  # służy do zapisywania binarnego plików
    with open(file_name, 'wb') as file:  # tryb wb też
        pickle.dump(dictionary, file)  # żeby słownik zapisywać do pliku


def create_medicine_and_add_to_dict(name, dose_per_pill, dose_per_day, current_amount):
    assert isinstance(name, str), 'name is supposed to be STR'
    assert isinstance(dose_per_pill, int), 'dose_per_pill is supposed to be INT'
    assert isinstance(dose_per_day, int), 'dose_per_day is supposed to be INT'
    assert isinstance(current_amount, int), 'current_amount is supposed to be INT'
    instance = Medicine(name, dose_per_pill, dose_per_day, current_amount)
    dict_of_instances[name] = instance


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


dict_of_instances = {}

create_medicine_and_add_to_dict('vetira_500', 500, 1500, 10)
create_medicine_and_add_to_dict('vetira_750', 750, 1500, 10)
create_medicine_and_add_to_dict('neurotop_600', 600, 1200, 40)


print(dict_of_instances)
# print(neurotop_600)
# poszukaj sposobu na to żeby podczas tworzenia instancji leku jednocześnie był on zapisywany do słownika
