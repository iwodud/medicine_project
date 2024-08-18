from functions_files import import_from_file, export_to_file
from functions_time import when_will_medicine_run_out
from functions_medicines import get_selected_medicine


def add_pills(medicine_name: str, amount_of_pills: int, file_name='data.json'):
    """Adds more pills to chosen medicine in file (you use when you bought new package for example)"""
    if not isinstance(medicine_name, str):
        raise TypeError('medicine_name must be a string')
    if not isinstance(amount_of_pills, int):
        raise TypeError('amount_of_pills must be an integer')
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    instances_dict = import_from_file()
    instances_dict[medicine_name]['amount_of_pills'] += amount_of_pills
    instances_dict[medicine_name]['amount_of_mg'] += amount_of_pills * instances_dict[medicine_name]['mg_per_pill']
    export_to_file(instances_dict)


def remove_medicine_from_dict(dict_name, medicine_name):
        """Removes given key (medicine_name) from given dictionary (dict_name). Returns None"""
        assert isinstance(dict_name, dict), 'dict_name is supposed to be a dictionary'
        try:
            del dict_name[medicine_name]
            return True
        except KeyError:
            print(f'Key "{medicine_name}" was not found in dictionary')
            return False


def remove_medicine_from_file(key: str, file_name='data.json'):
    """Removes chosen medicine basing on name (key) from dictionary in file. By default, it removes medicine from data.json"""
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')
    
    instances_dict = import_from_file()
    successfull = remove_medicine_from_dict(instances_dict, key)
    if successfull:
        export_to_file(instances_dict)


def check_single_information(medicine, file_name='data.json'):
    date_data = when_will_medicine_run_out(medicine)
    medicine_data = get_selected_medicine(medicine, file_name)
    daily_dose = medicine_data[0]['daily_dose']
    print(f"""
{medicine}
days left: {date_data[1]} 
finish date: {date_data[0]}
daily dose: {daily_dose}""")


def check_information():
    data = import_from_file()
    for medicine in data:
        check_single_information(medicine)


def change_daily_dose(medicine_name: str, new_daily_dose: int):
    """Changes daily dose of chosen medicine. You have to change daily dose of every medicine separately"""
    if not isinstance(medicine_name, str):
        raise TypeError('medicine_name must be a string')
    if not isinstance(new_daily_dose, int):
        raise TypeError('new_daily_dose must be an integer')
    
    try:
        instances_dict = import_from_file()
        instances_dict[medicine_name]['daily_dose'] = new_daily_dose
        export_to_file(instances_dict)
    except KeyError:
        print('The name of medicine is wrong. Check if it contains dose of a pill.\n')


def create_medicine():
    print('give following information\n')
    medicine_name = input('medicine name: ')
    pill_dose = int(input('dose per pill: '))
    daily_dose = int(input('daily dose: '))
    initial_amount = int(input('initial amount of pills'))
    name_of_instance = f'{medicine_name}_{pill_dose}'
    

def run():
    print('HELLO!')
    while True:
        choice = input('''Chose your action:
    1. Check information about all medicines
    2. Check information about single medicine
    3. Add pills to chosen medicine
    4. Change daily dose of selected medicine
    5. Create medicine
    6. Remove medicine
    
    Your action: ''')
    
        if choice == '1':
            check_information()
        elif choice == '2':
            medicine = input('Give name of medicine: ')
            check_single_information(medicine)
        elif choice == '3':
            try:
                medicine = input('Give name of medicine: ')
                amount_of_pills = int(input('Give amount of pills: '))
                add_pills(medicine, amount_of_pills)
            except KeyError:
                print('The name of medicine is wrong. Check if it contains dose of a pill.')
        elif choice == '4':
            medicine = input('Give name of medicine: ')
            new_daily_dose = int(input('Give new daily dose: '))
            change_daily_dose(medicine, new_daily_dose)
        elif choice == '5':
            pass
        elif choice == '6':
            medicine = input('Give name of medicine you want to remove: ')
            remove_medicine_from_file(medicine)
        else:
            print('\nWrong value, try again.\n')
            continue
        
        does_continue = input("""
Do you wan't to continue? If yes type 'y'. If not, press any other button.
Your choice: """)
        if does_continue.lower() == 'y':
            continue
        else:
            print('\nGOOD BYE!')
            break    
