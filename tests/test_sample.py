import pytest
from src.medicine.medicine import Medicine


vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)


@pytest.mark.parametrize(('val', 'expected'), (
    (vetira_500, 5000),
    (vetira_750, 7500),
    (neurotop_600, 24000)
))
def test_how_much_in_mg_single(val, expected):
    assert how_much_in_mg(val) == expected


@pytest.mark.parametrize(('vals', 'expected'), (
    ((vetira_750, vetira_500), 12500),
))
def test_how_much_in_mg_multu(vals, expected):
    assert how_much_in_mg(*vals) == expected



# @pytest.mark.parametrize('val', (4, 6, 8, 9))
# def test_how_much_in_mg_false(val):
#     assert not how_much_in_mg(val)


# def test_how_much_in_mg_type():
#     with pytest.raises(TypeError, match='Invalid type provided'):
#         how_much_in_mg('asdasdasd')
