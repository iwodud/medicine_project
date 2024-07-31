import json
from typing import List
from medicine import Medicine


def export_to_file(file_name: str, items: List[Medicine]):
    with open(file_name, 'w') as f:
        json.dump([item.serialize() for item in items], f, indent=4)


def import_from_file(file_name: str) -> List[Medicine]:
    with open(file_name) as f:
        return [Medicine(**item) for item in json.load(f)]


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


vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)
lacosamide_100 = Medicine('lacosamide', 100, 200, 50)


def run():
    """This function is the only function that you use if you want to check informations about medicines"""
    # Trzeba będzie na końcu ostro rozbudować
    data = import_from_file('instances.json')
    neurotop_600.remove_instance_from_file()
    print(import_from_file('instances.json'))

    print(data['lacosamide_100'][1])


# if __name__ == '__main__':
#     run()
