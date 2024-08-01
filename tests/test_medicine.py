import pytest
from src.medicine.medicine import Medicine


class TestMedicine:
    def test_create_medicine(self):
        apap_500 = Medicine('apap', 500, 500, 100)
        assert isinstance(apap_500, Medicine)
        assert apap_500.name == 'apap'
        assert apap_500.dose == 500
        assert apap_500.daily_dose == 500
        assert apap_500.initial_amount == 100