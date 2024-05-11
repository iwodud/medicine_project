import calendar
import datetime

# import datemath

# might be useful
# print(calendar.monthcalendar(2024, 5))
# print(calendar.monthrange(2024, 5))
# today = datetime.date.today()
# delta = datetime.timedelta(days=31)

today = datetime.date.today()
delta = datetime.timedelta(days=31)

today = datetime.date.today()
delta = datetime.timedelta(days=7)
print(today + delta)

# print(today + delta)

birthday = datetime.date(2024, 5, 29)

till_bday = birthday - today
print(till_bday)

'''
pomysły: funkcja dodawania pudełka/listka lub po prostu dodawanie x tabletek

konieczne funkcje: 
    4. Obliczanie ilości dni do wyczerpania zapasu z daną dawką dzienną i daną ilością leku w dawce (może *args będzie 
    dobre żeby można było do jednej funkcji wrzucić ten sam lek w różnych dawkach na tabletkę czyli dwie instancje)
    Chyba wtedy trzebaby zrobić krotki, pomyśl jak to zrobić.
    
    1. Funkcja przyjmująca ilość tabletek i zwracająca ilość w miligramach - done
    
    2. Funkcja przyjmująca dwie tabletki o różnych dawkach i zamieniająca na jedną - done
    
    3. Metoda obliczająca obecną ilość leku
        3.0 Funkcja do tworzenia instancji leku i przy okazji słownika
        3.1 Metoda tworząca słownik {lek: (ilość_leku_w_mg, data)}
        3.2 Metoda zapisująca przy stworzeniu instancji do pliku ile jest leku
        3.3 Metoda aktualizująca przy dodaniu leku dane w pliku
'''