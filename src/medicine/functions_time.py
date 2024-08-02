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