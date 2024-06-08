Wtyczka do QGIS - PyQGIS
Autorzy: Adam Orzeszek i Julia Konowrocka

Wtyczka służy do obliczania przewyższeń i pól powierzchni. Skonstruowana w Qt Designer dla wersji QGIS 3.34.5 i 3.36.3 i w tych
wersjach przetestowana. Obsługa polega na tym, że użytkownik musi umieścić folder z wtyczką w folderze "plugins" w swoim profilu QGIS (w moim przypadku ścieżka to 
C:\Users\orzes\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins). Następnie użytkownik wgrywa jakąś warstwę, na której są zaznaczone punkty, 
po czym może uruchomić wtyczkę i dokonać dwóch obliczeń:

1) przewyższenia - użytkownik zaznacza dwa punkty na warstwie, którą ustawił we wtyczkce jako aktualną, po czym klika przycisk
"OBLICZ PRZEWYŻSZENIE", wynik pojawia się w linijce: WYNIK: wynik w metrach

2) pola powierzchni - użytkownik zaznacza co najmniej 3 punkty na warstwie, którą ustawił we wtyczce jako aktualną, po czym może wybrać,
w jakiej jednostce ma zostać zwrócony wynik (domyślna to metry kwadratowe), a następnie klika przycisk "OBLICZ POLE POWIERZCHNI",
wynik pojawia się w linijce: WYNIK: wynik w wybranej jednostce

Dodatkowymi funkcjonalności są:
1) wspomniana możliwość ustawienia jednostka dla wyniku obliczenia pola powierzchni - metry kwadratowe, ary albo hektary
2) kasacja wyniku z konsoli wynikowej
3) kasacja zaznaczenia punktów na warstwie

Nie znaleźliśmy żadnej wady wtyczki albo jakiegokolwiek nieprawidłowego jej działania.

MIŁEGO KORZYSTANIA Z PROGRAMU! :)

P.S. zachęcamy do sprawdzenia ikonki wtyczki - została wstawiona autorska ikonka. Mała rzecz, a cieszy.
