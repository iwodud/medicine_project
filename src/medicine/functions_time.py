import datetime as dt


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
    """returns how much mg of medicine you need for given number of days"""
    if not (isinstance(number_of_days, int) and isinstance(daily_dose_in_mg, int)):
        raise TypeError('arguments must be integers')
    if number_of_days <= 0 or daily_dose_in_mg <= 0:
        raise ValueError('arguments must be greater than zero')
    
    return number_of_days * daily_dose_in_mg


def how_much_days_enough(daily_dose: int, amount_of_mg: int) -> int:
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