import datetime as dt
import json

class Medicine:
    """Class Medicine contains arguments necessary to calculate time after which the medicine will run out.

    Args:
        name (str): name of medicine with it`s dose per pill (for instance apap_600)
        dose (int): dose of one pill (for apap_600 it's 600)
        daily_dose ((int, float)): dose of medicine you take per day
        current_amount (int): amount of pills you have at the moment

    Methods:
        __init__(self, name, dose, daily_dose, current_amount): initializes arguments
        __str__(self): describes instance nicely
        __repr__(self): describes instance concretely
        add_medicine_to_dict(self, dict_name): adds name of an instance (self.name) to dictionary with a given name (dict_name)
        append_instance_to_file(self, file_name='json'): appends instance of Medicine to dictionary in file (default json). If file doesn't exist, creates the file
        add_pills(self, amount_of_pills): not ready yet
        current_mg(self): basing on self.current_amount returns amount of the medicine in milligrams
    """
    instances = {}  # dictionary before __init__ is shared by all instances

    def __init__(self, name: str, dose: int | float, daily_dose: int | float, current_amount: int):
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
        self._add_medicine_to_dict(self.instances)
        self._append_instance_to_file()
    
    
    def _add_medicine_to_dict(self, dict_name):
        """Adds name_dose of an instance (self.name + _ + self.dose), with tuple (self.current_mg(), dt.date.today()) 
        as value, to dictionary with a given name (dict_name)"""
        assert isinstance(dict_name, dict), 'dict_name id supposed to be DICT'
        dict_name[str(self.name) + '_' + str(self.dose)] = {'amount_of_mg': self.current_mg(), 'date': str(dt.date.today())}
    
    
    def _remove_medicine_from_dict(self, dict_name, key):
        """Removes given key (key) from given dictionary (dict_name). Returns None"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be a DICT'
        try:
            del dict_name[key]
        except KeyError:
            print(f'Key "{key}" was not found in dictionary')
        return None


    def _append_instance_to_file(self, file_name='instances.json'):
        """Appends instance of Medicine to dictionary in file (default instances.json). If file doesn't exist, creates the file"""
        assert isinstance(file_name, str), 'file_name is supposed to be STR'
        try:
            with open(file_name, 'r') as file:
                instances_dict = json.load(file)
        except (FileNotFoundError, EOFError):
            instances_dict = {}

        self._add_medicine_to_dict(instances_dict)

        with open(file_name, 'w') as file:
            json.dump(instances_dict, file, indent=4)
    
    
    def remove_instance_from_file(self, key=None, file_name='instances.json'):
        """Removes instance of Medicine basing on name (key) from dictionary in file. By default it removes itself from instances.json"""
        assert isinstance(file_name, str), 'file_name is supposed to be STR'
        if key is None:
            key = str(self.name) + '_' + str(self.dose)
        try:
            with open(file_name, 'r') as file:
                instances_dict = json.load(file)
        except (FileNotFoundError, EOFError):
            print(f'File {file_name} doesn\'t exist')
            return None

        self._remove_medicine_from_dict(instances_dict, key)

        with open(file_name, 'w') as file:
            json.dump(instances_dict, file)


    def add_pills(self, amount_of_pills):  # funkcja jeszcze nie gotowa, trzeba ją rozbudować (i to porządnie), tego komentarza nie usuwaj
        """Adds more pills to an instance (for example you bought package of pills and add it to the data base)"""  # nie jestem pewien czy ta funkcja będzie tutaj
        assert isinstance(amount_of_pills, int), 'amount_of_pills is supposed to be INT'
        self.current_amount += amount_of_pills


    def current_mg(self):
        """Basing on self.current_amount returns amount of the medicine in milligrams"""
        amount_of_pills = self.current_amount
        mg_per_pill = self.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        return amount_of_mg


    def __str__(self):
        return f'{self.name.title()} medicine with dose {self.dose} mg per pill (daily dose {self.daily_dose} mg) has {self.current_amount} pills left.'


    def __repr__(self):
        return f'Medicine({self.name}, {self.dose}, {self.daily_dose}, {self.current_amount})'


def how_much_in_mg(*medicines: Medicine):
    """Takes medicine's names (STR) and returns amount of the medicine in milligrams"""
    sum_of_mg = []  # to this list I add milligrams multiplied by the number of pills
    for medicine in medicines:
        assert isinstance(medicine, Medicine), 'medicines is supposed to be medicine.Medicine'
        amount_of_pills = medicine.current_amount
        mg_per_pill = medicine.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        sum_of_mg.append(amount_of_mg)
    return sum(sum_of_mg)