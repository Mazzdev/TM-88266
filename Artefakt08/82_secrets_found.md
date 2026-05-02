\# RAPORT ANALIZY WYCIEKÓW DANYCH



\## Identyfikacja



Audytor: Dominik  

Numer indeksu: 88266  

Projekt: ApiDemos



\## Top 3 zagrożenia



1\. \*\*Adresy URL\*\*

&#x20;  - Mogą ujawniać endpointy serwerów lub środowiska testowe.



2\. \*\*Słowa kluczowe typu token / secret / password\*\*

&#x20;  - Mogą wskazywać na potencjalne dane dostępowe zapisane w kodzie.



3\. \*\*Adresy IP\*\*

&#x20;  - Mogą ujawniać infrastrukturę lub prywatne adresy usług.



\## Top 3 False Positives



1\. \*\*Standardowe linki dokumentacyjne\*\*

&#x20;  - Często są bezpieczne i służą tylko jako odnośniki do dokumentacji.



2\. \*\*Nazwy stringów interfejsu\*\*

&#x20;  - Mogą zawierać słowo password, ale oznaczają jedynie etykietę pola hasła.



3\. \*\*Linki do bibliotek Androida\*\*

&#x20;  - Same w sobie nie oznaczają wycieku sekretu.



\## Wniosek



Wyniki skanera wymagają ręcznej analizy. Nie każde znalezisko jest realnym wyciekiem,

ale każde powinno zostać zweryfikowane przed publikacją aplikacji.

