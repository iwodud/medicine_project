from icecream import ic
import datetime as dt
import pickle

class Medicine:
    """Class Medicine contains arguments necessary to calculate time after which the medicine will run out.

    Args:
        name (str): name of medicine with it`s dose per pill (for instance apap_600)
        dose (int): dose of one pill (for apap_600 it's 600)
        daily_dose ((int, float)): dose of medicine I take per day
        current_amount (int): amount of pills I have at the moment

    Methods:
        __init__(self, name, dose, daily_dose, current_amount): initializes arguments 
        __str__(self): describes instance nicely
        __repr__(self): describes instance concretely
        add_medicine_to_dict(self, dict_name): adds name of an instance (self.name) to dictionary with a given name (dict_name)
        append_instance_to_file(self, file_name='instances.p'): appends instance of Medicine to dictionary in file (default instances.p). If file doesn't exist, creates the file
        add_medicine(self, amount_of_pills): not ready yet
        how_much_in_mg(self): basing on self.current_amount returns amount of the medicine in milligrams
    """
    instances = {}  # dictionary before __init__ is shared by all instances
    
    def __init__(self, name, dose, daily_dose, current_amount):  # initializes attributes
        self.__name = name  # podwójny podkreślnik sprawia, że atrybut staje się prywatny i żeby do niego dotrzeć trzeba to zrobić przez getter/setter albo się nagimnastykować
        self.__dose = dose  # to nie dotyczy metod z podwójnymi podkreślnikami z obu stron np. __init__(), to są metody specjalne
        self.__daily_dose = daily_dose
        self.__current_amount = current_amount
        self.add_medicine_to_dict(self.instances)
        self.append_instance_to_file()
    
    
    @property  # @property to dekorator do tworzenia automatycznych getterów, jak nie wiesz co to dekorator to olej to
    def name(self):
        return self.__name
    
    
    @name.setter  # tutaj to samo tylko do setterów. można sobie poustawiać rzeczy w setterze. Trzeba taki cyrk robić z każdym atrybutem niestety :/
    def name(self, var):
        assert isinstance(var, str), 'name is supposed to be STR'
        try:
            self.__name = var
        except Exception as e:  # protects from other errors than TypeError protected by "assert"
            print(e)
    
    
    @property
    def dose(self):
        return self.__dose
    
    
    @dose.setter
    def dose(self, var):
        assert isinstance(var, int), 'dose is supposed to be INT'
        try:
            self.__dose = var
        except Exception as e:
            print(e)
    
    
    @property
    def daily_dose(self):
        return self.__daily_dose
    
    
    @daily_dose.setter
    def daily_dose(self, var):
        assert isinstance(var, (int, float)), 'daily_dose is supposed to be INT or FLOAT'
        try:
            self.__daily_dose = var
        except Exception as e:
            print(e)
    
    
    @property
    def current_amount(self):
        return self.__current_amount
    
    
    @current_amount.setter
    def current_amount(self, var):
        print('You should use other function to change amount of medicine')  # reminder for not using this function
        assert isinstance(var, (int, float)), 'current_amount is supposed to be INT or FLOAT'
        try:
            self.__current_amount = var
        except Exception as e:
            print(e)
    
    
    def add_medicine_to_dict(self, dict_name):
        """Adds name_dose of an instance (self.name + _ + self.dose), with tuple (self.how_much_in_mg(), dt.date.today()) 
        as value, to dictionary with a given name (dict_name)"""
        assert isinstance(dict_name, dict), 'dict_name id supposed to be DICT'
        dict_name[str(self.name) + '_' + str(self.dose)] = (self.how_much_in_mg(), dt.date.today()) ## ogarnij drugi argument krotki !!!
    
    
    def append_instance_to_file(self, file_name='instances.p'):
        """Appends instance of Medicine to dictionary in file (default instances.p). If file doesn't exist, creates the file"""
        assert isinstance(file_name, str), 'file_name is supposed to be STR'
        try:
            with open(file_name, 'rb') as file:
                instances_dict = pickle.load(file)
        except (FileNotFoundError, EOFError):
            instances_dict = {}

        self.add_medicine_to_dict(instances_dict)

        with open(file_name, 'wb') as file:
            pickle.dump(instances_dict, file)
    
    
    def add_medicine(self, amount_of_pills):  # funkcja jeszcze nie gotowa, trzeba ją rozbudować (i to porządnie), tego komentarza nie usuwaj
        """Adds more pills to an instance"""
        assert isinstance(amount_of_pills, int), 'amount_of_pills is supposed to be INT'
        self.current_amount += amount_of_pills
    
    
    def how_much_in_mg(self):
        """Basing on self.current_amount returns amount of the medicine in milligrams"""
        amount_of_pills = self.current_amount
        mg_per_pill = self.dose
        amount_of_mg = amount_of_pills * mg_per_pill
        return amount_of_mg
    
    
    def __str__(self):  # __str__() i __repr__() używam z przyzwyczajenia, tak mi wpojono. W docstringu masz co robią. 
        return f'{self.name.title()} medicine with dose {self.dose} mg per pill (daily dose {self.daily_dose} mg) has {self.current_amount} pills left.'
    
    
    def __repr__(self):
        return f'Medicine({self.name}, {self.dose}, {self.daily_dose}, {self.current_amount})'
