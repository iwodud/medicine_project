class Medicine:
    """Contains arguments necessary to calculate time after which the medicine will run out."""

    def __init__(self, name: str, dose: int | float, daily_dose: int | float, current_amount: int):
        """Create a medicine instance.

        :param str name: The name of the medicine
        :param int|float dose: The dose (in mg) in a single pill
        :param int|float daily_dose: The dose (in mg) to be taken daily
        :param int current_amount: the current amount of pills available
        """
        if not isinstance(name, str):
            raise ValueError('name is supposed to be a string')
        self.name = name

        if not isinstance(dose, (int, float)):
            raise ValueError('dose is supposed to be a number')
        if dose < 0:
            raise ValueError('Negative doses do not exist')
        self.dose = dose

        if not isinstance(daily_dose, (int, float)):
            raise ValueError('daily_dose is supposed to be a number')
        if dose < 0:
            raise ValueError('Negative doses do not exist')
        self.daily_dose = daily_dose

        if not isinstance(current_amount, int):
            raise ValueError('current_amount is supposed to be an integer')
        if current_amount < 0:
            raise ValueError('It is not possible to have negative amounts of pills')
        self.current_amount = current_amount

    def serialize(self):
        return {'name': self.name, 'dose': self.dose, 'daily_dose': self.daily_dose, 'current_amount': self.current_amount}

    @property
    def current_mg(self):
        """Get the total amount of remaining medicine, in mg."""
        return self.current_amount * self.dose

    @property
    def daily_pills(self):
        # TODO: To nie koniecznie dobrze zadziała. Trzeba rozważyć co się stanie jeżeli:
        # dawka dzienna nie dzieli się bez reszty (np. codziennie ma być brane 12mg, a pigułka ma 5mg)
        return self.daily_dose / self.dose

    @property
    def days_left(self):
        """Get the remaining number of days before the medicine runs out."""
        # TODO: to będzie zwrócone jako ułamkowa liczba, co niekoniecznie jest to co byś chciał,
        # return round(self.current_mg / self.daily_dose)  # Jeżeli ma być zaokrąglane
        # return self.current_mg // self.daily_dose  # Jeżeli ma być zaokrąglane w dół
        return self.current_mg / self.daily_dose

    def add_pills(self, amount: int):
        self.current_amount += amount

    def take_dose(self):
        # TODO: Jak obsłuzyć braki?
        # jak jest mniej pigułek niż trzeba, to wezmniejsz tylko tyle ile jest. Inna opcja,
        # to jeżeli nie starczy ci, to poprostu tego dnia nie bierzesz
        pills = min(self.current_amount, self.daily_pills)
        self.current_amount -= pills

    def __str__(self):  # __str__() i __repr__() używam z przyzwyczajenia, tak mi wpojono. W docstringu masz co robią.
        return f'{self.name.title()} with dose {self.dose} mg per pill (daily dose {self.daily_dose} mg) has {self.current_amount} pills left.'

    def __repr__(self):
        return f'Medicine({self.name}, {self.dose}, {self.daily_dose}, {self.current_amount})'
