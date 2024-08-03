import datetime as dt

from functions_medicines import get_selected_medicine

def to_date_type(medicine: str) -> dt.date:
    """changes string containing date (year-month-day format) to datetime.date type. doesn't change type permantently."""
    if not isinstance(medicine, str):
        raise TypeError('medicine must be a string')
    try:
        date = dt.datetime.strptime(medicine, "%Y-%m-%d").date()
        return date
    except ValueError:
        raise ValueError("The date string must be in 'YYYY-MM-DD' format and represent a valid date.")


def how_many_days_passed(given_date: str) -> int:
    if not isinstance(given_date, str):
        raise TypeError('given_date must be a string')

    current_date = dt.datetime.now().date()
    days_passed = current_date - to_date_type(given_date)
    return days_passed.days


def days_to_amount_of_medicine(number_of_days: int, daily_dose_in_mg: int):  # pomyśl nad lepszą nazwą
    """returns how much mg of medicine you need for given number of days"""  # ile leku potrzebujesz na X dni
    if not (isinstance(number_of_days, int) and isinstance(daily_dose_in_mg, int)):
        raise TypeError('arguments must be integers')
    if number_of_days <= 0 or daily_dose_in_mg <= 0:
        raise ValueError('arguments must be greater than zero')
    
    needed_mg_of_medicine = number_of_days * daily_dose_in_mg
    return needed_mg_of_medicine


def how_much_days_is_enough(daily_dose: int, amount_of_mg: int) -> int:  # na ile dni starczy leku
    """Returns number of days for which the medicine is enough / after which the medicine will run out"""
    if not (isinstance(daily_dose, int) and isinstance(amount_of_mg, int)):
        raise TypeError('daily_dose and amount_of_mg must be integers')
    if daily_dose < 0 or amount_of_mg < 0:
        raise ValueError('given values can\'t be negative')
    
    try:
        number_of_days_enough = amount_of_mg // daily_dose
        return number_of_days_enough
    except ZeroDivisionError:
        return 'daily dose can\'t be equal to zero'


def when_will_medicine_run_out(medicine_name: str, file_name='data.json') -> tuple[dt.date, int]:
    """basing on given name, function returns date when the medicine will run out and how many days are left 
    in a tuple (date, number of days for medicine to run out)."""
    if not isinstance(medicine_name, str):
        raise TypeError('medicine_name must be an integer')
    
    medicine_data = get_selected_medicine(medicine_name, file_name)
    
    starting_day_str = medicine_data[0]['initialization_date']
    starting_day_date = to_date_type(starting_day_str)
    
    daily_dose = medicine_data[0]['daily_dose']
    
    amount_of_mg = medicine_data[0]['amount_of_mg']
    number_of_days = how_much_days_is_enough(daily_dose, amount_of_mg)
    
    delta = dt.timedelta(days=number_of_days)
    when_will_run_out = starting_day_date + delta
    
    return (when_will_run_out, number_of_days)

print(when_will_medicine_run_out('ibuprofe'))