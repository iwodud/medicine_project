## Pomysły:

* funkcja dodawania pudełka/listka lub po prostu dodawanie x tabletek

## Poprawki na teraz:

1. [ ] Ogranicz zapis i odczyt pliku do dwóch funkcji

2. [ ] Zmień pickle na JSON

3. [ ] Wyrzuć z klasy tyle funkcji ile można, resztę zostaw poza nią

4. [ ] Ogarnij testy

## Konieczne funkcje:

1. [x] Funkcja przyjmująca ilość tabletek i zwracająca ilość w miligramach

2. [x] Funkcja przyjmująca dwie tabletki o różnych dawkach i zamieniająca na jedną

3. Metoda obliczająca obecną ilość leku
   [x] 3.0 Funkcja do tworzenia instancji leku i przy okazji słownika
   [x] 3.1 Metoda tworząca słownik {lek: (ilość_leku_w_mg, data dodania/modyfikacji)} (w zależności od tego czy przy tworzeniu leku czy przy dodawaniu)
       [x] 3.1.2 Ogarnij dobre formatowanie daty w krotce w słowniku
   [x] 3.2 Metoda zapisująca przy stworzeniu instancji do pliku ile jest leku (przerzuć z main_program)
   [x] 3.3 Metoda usuwająca z pliku instancję leku
   [ ] 3.4 Metoda aktualizująca przy dodaniu leku dane w pliku (rozbuduj metodę add_medicine)

4. [ ] Obliczanie ilości dni do wyczerpania zapasu z daną dawką dzienną i daną ilością leku w dawce (może *args będzie
   dobre żeby można było do jednej funkcji wrzucić ten sam lek w różnych dawkach na tabletkę czyli dwie instancje)
   Chyba wtedy trzebaby zrobić krotki, pomyśl jak to zrobić.
