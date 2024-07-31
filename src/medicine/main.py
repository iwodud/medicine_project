import json
from typing import List
from medicine import Medicine


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


paracetamol_500 = Medicine('paracetamol', 500, 1500, 100)
paracetamol_750 = Medicine('paracetamol', 750, 1500, 100)
ibuprofen_600 = Medicine('ibuprofen', 600, 1200, 40)
aspiryna_100 = Medicine('aspiryna', 100, 200, 50)


def run():
    """This function is the only function that you use if you want to check informations about medicines"""
    pass  # Trzeba będzie na końcu ostro rozbudować


if __name__ == '__main__':
    run()
