import json
from typing import List
from medicine.medicine import Medicine


def export_to_file(filename: str, items: List[Medicine]):
    with open(filename, 'w') as f:
        json.dump([item.serialize() for item in items], f, indent=4)


def import_from_file(filename: str) -> List[Medicine]:
    with open(filename) as f:
        return [Medicine(**item) for item in json.load(f)]


def how_much_in_mg(*medicines):
    """Takes medicine's names (STR) and returns amount of the medicine in milligrams"""
    # Ja wolę taki zapis, ale obie działają równie dobrze
    # return sum([medicine.current_mg for medicine in medicines])
    sum_of_mg = []  # to this list I add milligrams multiplied by the number of pills
    for medicine in medicines:
        sum_of_mg.append(medicine.current_mg)
    return sum(sum_of_mg)


vetira_500 = Medicine('vetira', 500, 1500, 10)
vetira_750 = Medicine('vetira', 750, 1500, 10)
neurotop_600 = Medicine('neurotop', 600, 1200, 40)
lacosamide_100 = Medicine('lacosamide', 100, 200, 50)


def run():
    data = import_from_file('instances.json')

    # Tu różne operacje które dodają/usuwają/zmieniają stan różnych leków.
    # Można za każdym razem zapisać do pliku, albo tylko raz na końcu. Obie
    # podejścia mają swoje wady i zalety:
    #
    # Zapis za każdym razem jest wolniejszy (aczkolwiek w tym przypadku to nie istotne), ale jak np.
    # byś to robił tak że ci wypisuje co masz brać lek po leku, i przy każdym leku zatwierdzasz że wziąłeś,
    # to dobrze by było po każdym zatwierdzeniu zapisać.
    #
    # Jeżeli to ma działać bardziej na zasadzie że wypisujesz całą listę, a na końcu potwierdzasz że wszystko
    # wziąłeś, to zapisz na końcu.
    #
    # Ogólna idea jest taka, że zapis powinien być wtedy i tylko wtedy kiedy jesteś pewny że cały zbiór operacji
    # jest gotowe do zapisu. Trzeba pamiętać o tym że w każdej chwili program się może wykrzaczyc, i wszysktko
    # co nie było zapisane do tego czasu zniknie

    for medicine in sorted(data, key=lambda m: m.name):
        print(medicine)
    print(f'In total {how_much_in_mg(*data)}mg left')

    export_to_file('instances.json', data)


if __name__ == '__main__':
    run()
