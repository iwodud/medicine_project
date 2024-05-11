import pytest
from medicine_classes import Medicine

vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)

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

print(how_much_in_mg(vetira_500, vetira_750))

@pytest.mark.parametrize(('val', 'expected'), ((vetira_500, 5000), (vetira_750, 7500), ((vetira_750, vetira_500), 12500), (neurotop_600, 24000)))
def test_how_much_in_mg(val, expected):
    assert how_much_in_mg(val) == expected


# @pytest.mark.parametrize('val', (4, 6, 8, 9))
# def test_how_much_in_mg_false(val):
#     assert not how_much_in_mg(val)


# def test_how_much_in_mg_type():
#     with pytest.raises(TypeError, match='Invalid type provided'):
#         how_much_in_mg('asdasdasd')
