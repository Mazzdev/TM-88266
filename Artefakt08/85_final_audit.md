\# RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS



\*\*Data:\*\* 14.03.2026  

\*\*Audytor:\*\* Dominik, nr indeksu 88266  

\*\*Projekt:\*\* ApiDemos



\---



\## 1. OCENA KOŃCOWA — SECURITY SCORE



\*\*Wynik:\*\* 0/100  

\*\*Status:\*\* REJECTED



Aplikacja nie powinna zostać zaakceptowana bez poprawek bezpieczeństwa.



\---



\## 2. KLUCZOWE OBSZARY RYZYKA



\### A. Konfiguracja systemowa — Zadanie 8.1



\*\*Problem:\*\*  

Manifest aplikacji zawiera potencjalnie ryzykowne uprawnienia oraz wymaga kontroli flagi debugowania.



\*\*Wpływ:\*\*  

Nadmierne uprawnienia zwiększają ryzyko naruszenia prywatności użytkownika.



\---



\### B. Wycieki danych — Zadanie 8.2



\*\*Problem:\*\*  

Skaner wykrył potencjalne adresy URL, słowa kluczowe oraz inne dane mogące wskazywać na hardcoded secrets.



\*\*Wpływ:\*\*  

Zakodowane na stałe dane mogą zostać odczytane po dekompilacji APK.



\---



\### C. Biblioteki zewnętrzne — Zadanie 8.3



\*\*Problem:\*\*  

Wykryto podatne lub przestarzałe biblioteki z poziomami HIGH, CRITICAL oraz MEDIUM.



\*\*Wpływ:\*\*  

Podatne zależności mogą umożliwiać ataki na aplikację bez modyfikowania jej kodu źródłowego.



\---



\### D. Klasyfikacja ryzyka — Zadanie 8.4



\*\*Problem:\*\*  

Security Score spadł do bardzo niskiego poziomu.



\*\*Wpływ:\*\*  

Aplikacja wymaga natychmiastowych poprawek przed publikacją.



\---



\## 3. MAPA DROGOWA NAPRAWCZA



1\. \*\*Priorytet 1:\*\* Zaktualizować podatne biblioteki do bezpiecznych wersji.

2\. \*\*Priorytet 1:\*\* Zweryfikować i usunąć niepotrzebne uprawnienia z AndroidManifest.xml.

3\. \*\*Priorytet 2:\*\* Przenieść potencjalne sekrety poza kod aplikacji.

4\. \*\*Priorytet 2:\*\* Upewnić się, że `debuggable=false` w wersji produkcyjnej.



\---



\## WNIOSKI KOŃCOWE



Na podstawie wykonanej analizy statycznej aplikacja ApiDemos wymaga poprawek bezpieczeństwa.

Największe ryzyko stanowią przestarzałe biblioteki oraz potencjalne wycieki danych.

Rekomendacja audytora: \*\*NO-GO / REJECTED\*\* do czasu usunięcia krytycznych problemów.

