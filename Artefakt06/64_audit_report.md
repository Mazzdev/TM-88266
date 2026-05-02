\# RAPORT AUDYTU ARCHITEKTURY POM



\## 1. Analiza spójności



Framework POM korzysta z mapy selektorów wygenerowanej w Artefakcie 05.

Klasa BasePage ładuje plik 53\_selectors.json, a MainPage korzysta z tych danych przez metodę get\_selector().



Użyte selektory, takie jak ADD, ACTION\_BAR\_TITLE oraz IMAGE, są pobierane z jednej centralnej mapy.

Dzięki temu testy nie zawierają twardo wpisanych identyfikatorów UI.



\## 2. Ocena modularności



Architektura jest modularna, ponieważ BasePage odpowiada za ładowanie selektorów,

MainPage za logikę ekranu, a 63\_pom\_test.py za scenariusz testowy.



Jeśli deweloper zmieni ID przycisku ADD na PLUS\_BTN, wystarczy zaktualizować mapę selektorów

w pliku 53\_selectors.json. Kod testu i klasy MainPage nie muszą być przebudowywane,

o ile zachowany zostanie biznesowy klucz ADD.



\## 3. Wnioski optymalizacyjne



Do BasePage warto dodać mechanizm explicit wait, czyli oczekiwania na element.

Dzięki temu framework byłby bardziej odporny na wolniejsze ładowanie aplikacji

i mniejszą liczbę błędów typu flaky test.



Dodatkowo można dodać obsługę wyjątków dla brakujących selektorów oraz logowanie

każdej akcji użytkownika do osobnego pliku.

