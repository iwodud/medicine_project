import datetime as dt
import json

class Medicine:
    """Class Medicine contains arguments necessary to calculate time after which the medicine will run out.

    Args:
        name (str): name of medicine with it's dose per pill (for instance apap_600)
        dose (int, float): dose of one pill (for apap_600 it's 600)
        daily_dose (int, float): dose of medicine you take per day
        initial_amount (int, float): amount of pills you have at the moment

    Methods:
        __init__(self, name, dose, daily_dose, initial_amount): initializes arguments
        initial_mg(self): basing on self.initial_amount, the method returns amount of the medicine in milligrams.
        __str__(self): describes instance nicely
        __repr__(self): describes instance concretely
        
    Private Methods (These are NOT meant to be used outside of class. These are used once, during initialization of an instance):
        __add_medicine_to_dict(self, dict_name): adds name of an instance (self.name) and it's parameters to dictionary with a given name (dict_name).
        __append_instance_to_file(self, file_name='data.json'): appends instance of Medicine to dictionary in file (default data.json).
            If file doesn't exist, the method creates the file.
    """
    instances = {}  # dictionary before __init__ is shared by all instances

    def __init__(self, name: str, dose: int | float, daily_dose: int | float, initial_amount: int | float):
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

        if not isinstance(initial_amount, (int, float)):
            raise ValueError('initial_amount is supposed to be a number')
        if initial_amount < 0:
            raise ValueError('It is not possible to have negative amounts of pills')
        self.initial_amount = initial_amount
        self.__add_medicine_to_dict(self.instances)
        self.__append_instance_to_file()
    
    
    def __add_medicine_to_dict(self, dict_name):
        """Adds name_dose of an instance (self.name + _ + self.dose), with dictionary containing it's parameters as value, to dictionary with a given name (dict_name)"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be DICT'
        dict_name[str(self.name) + '_' + str(self.dose)] = {'daily_dose': self.daily_dose,'mg_per_pill': self.dose,
                                                            'amount_of_mg': self.initial_mg(), 'amount_of_pills': self.initial_amount, 
                                                            'initialization_date': str(dt.date.today())}


    def __append_instance_to_file(self, file_name='data.json'):
        """Appends instance of Medicine to dictionary in file (default data.json). If file doesn't exist, creates the file"""
        assert isinstance(file_name, str), 'file_name is supposed to be STR'
        try:
            with open(file_name, 'r') as file:
                instances_dict = json.load(file)
        except (FileNotFoundError, EOFError):
            instances_dict = {}

        self.__add_medicine_to_dict(instances_dict)

        with open(file_name, 'w') as file:
            json.dump(instances_dict, file, indent=4)


    def initial_mg(self):
        """Basing on self.initial_amount returns amount of the medicine in milligrams at the moment of creating the medicine"""
        amount_of_pills = self.initial_amount
        mg_per_pill = self.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        return amount_of_mg


    def __str__(self):
        return f'{self.name.title()} medicine with dose {self.dose} mg per pill (daily dose {self.daily_dose} mg) has {self.initial_amount} pills left.'


    def __repr__(self):
        return f'Medicine({self.name}, {self.dose}, {self.daily_dose}, {self.initial_amount})'
