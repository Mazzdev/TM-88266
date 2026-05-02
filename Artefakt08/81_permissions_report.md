\# Raport audytu uprawnień



\## Wynik

Skrypt przeanalizował plik AndroidManifest.xml i wygenerował raport RiskyPermission.xml.



\## Wnioski

Wykryte uprawnienia należy ocenić pod kątem zasady minimalnych uprawnień.

Jeśli aplikacja wymaga dostępu do kontaktów, SMS, lokalizacji lub kamery, powinno to wynikać z realnej funkcji aplikacji.



\## Ryzyko

Nadmierne uprawnienia mogą prowadzić do wycieku danych użytkownika albo nadużyć prywatności.



\## Rekomendacja

Usunąć nieużywane uprawnienia i upewnić się, że flaga debuggable nie jest ustawiona na true w wersji produkcyjnej.

