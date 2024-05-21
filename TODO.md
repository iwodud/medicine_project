## Pomysły:

* funkcja dodawania pudełka/listka lub po prostu dodawanie x tabletek

## Konieczne funkcje:

1. Funkcja przyjmująca ilość tabletek i zwracająca ilość w miligramach - done

2. Funkcja przyjmująca dwie tabletki o różnych dawkach i zamieniająca na jedną - done

3. Metoda obliczająca obecną ilość leku
   3.0 Funkcja do tworzenia instancji leku i przy okazji słownika - done
   3.1 Metoda tworząca słownik {lek: (ilość_leku_w_mg, data dodania/modyfikacji)} (w zależności od tego czy przy tworzeniu leku czy przy dodawaniu) - done
       3.1.2 Ogarnij dobre formatowanie daty w krotce w słowniku - done (jak się wyprintuje to wygląda inaczej niż w krotce)
   3.2 Metoda zapisująca przy stworzeniu instancji do pliku ile jest leku (przerzuć z main_program) - done
   3.3 Metoda usuwająca z pliku instancję leku - done
   3.4 Metoda aktualizująca przy dodaniu leku dane w pliku (rozbuduj metodę add_medicine)

4. Obliczanie ilości dni do wyczerpania zapasu z daną dawką dzienną i daną ilością leku w dawce (może *args będzie
   dobre żeby można było do jednej funkcji wrzucić ten sam lek w różnych dawkach na tabletkę czyli dwie instancje)
   Chyba wtedy trzebaby zrobić krotki, pomyśl jak to zrobić.
