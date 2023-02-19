# SeleniumPython

Testy napisane na potrzeby kursu Python + Selenium.

W tym repozytorium znajdują się skrypty testowe stworzone podczas zajęć.
Celem ich stworzenia było pokazanie sposobu w jaki działa Selenium WebDriver oraz zaprezentowanie na konkretnych przykładach dobrych oraz złych praktyk implementowania skryptów.

Elementy w poniższych skryptach nie powinny zostać użyte w projektach:
 - time.sleep(5) - zalecana praktyka to używanie inteligentnych waitów
	- Tworzenie WebDrivera (driver = webdriver.Chrome()) dla każdego testu osobno
	- Podawanie bezpośredniej ścieżki dla drivera przy inicjalizacji obiektu webdriver
	- Sztywne umieszczanie selektoów dla webelementów (zalecane POM lub stałe)
	- Pozostawianie zakomentowanego kodu
	- Dziwne nazwy zmiennych

Dobre praktyki:
	- Intuicyjne nazwy zmiennych, funkcji, klas - nazwa określająca cel napisania kodu
	- Dodawanie komentarzy (zwłaszcza w przypadku skomplikowanego kodu)
	- Implementacja funkcji dla poszczególnych funkcjonalności w osobnych plikach lub klasach
	- Używanie Fixtures (np. dla inicjalizacji drivera)

Na potrzeby zaliczenia tego kursu można wzorować się na tym pliku:
 - test_using_account_page_final.py (wymagany mały refactoring na potrzeby zaliczenia - np. dodanie stałych)

Pozostałe pliki są tylko pokazaniem jak doszliśmy do końcowego rozwiązania.
W celu zainstalowania projektu możecie użyć komendy:
pip install -r requirement.txt

Testy zostaną uruchomione po wpisaniu komendy:
pytest (w terminalu)

Niektóre przykładowe pliki mogą wymagać podmienienia ścieżki dla Chromedrivera (w ramach złych praktyk :)).

