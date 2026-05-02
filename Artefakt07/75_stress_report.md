\# RAPORT STABILNOŚCI I ODPORNOŚCI APLIKACJI



\## 1. Wyniki testów gestów



W teście 7.1 sprawdzono logikę gestu scroll/swipe opartą na procentowych współrzędnych ekranu.

Takie podejście zwiększa odporność testu na różne rozdzielczości urządzeń.



\*\*Wynik:\*\* PASS



\## 2. Odporność na przerwania



W teście 7.2 zasymulowano połączenie przychodzące.

Aplikacja przeszła przez stany:



\- ACTIVE

\- onPause

\- onResume



Po zakończeniu przerwania aplikacja odzyskała fokus.



\*\*Wynik:\*\* PASS



\## 3. Zarządzanie stanem urządzenia



W teście 7.3 wykonano zmianę orientacji:



\- PORTRAIT

\- LANDSCAPE

\- PORTRAIT



Dodatkowo zasymulowano zmianę stanu zasilania ekranu.



\*\*Wynik:\*\* PASS



\## 4. Synchronizacja



W teście 7.4 zastosowano mechanizm WebDriverWait.

Test odróżnia poprawne znalezienie elementu od przekroczenia czasu oczekiwania.



\*\*Wynik:\*\* PASS



\## 5. Wniosek końcowy



Na podstawie wykonanych testów aplikacja ApiDemos wykazuje dobrą przeżywalność w warunkach stresu systemowego.

Obsługuje gesty, przerwania, zmianę orientacji oraz synchronizację bez krytycznych błędów.

