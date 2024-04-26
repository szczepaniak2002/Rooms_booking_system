# Rooms_booking_system
## O projekcie
Projekt dotyczy stworzenia strony internetowej w Django. 
Jest to strona, na której możemy szukać dotępnych do wynajęcia pokoi, używająć różnych filtrów, rezerwować wybrane i dostępne pokoje, zarządzać swoimi rezerwacjami itd. Projekt podpięty jest do bazy danych, w której przechowywane są wszystkie informacje o pokojach i użytkownikach. Przy wchodzeniu na stronę, musimy się zalogować do swojego konta, a jeśli takiego nie posiadamy, możemy się zarejestrować i stworzyć swoje indywidualne konto. 

#### Oto podgląd strony w formie screenów: 
![Zrzut ekranu 2024-04-26 123425](https://github.com/szczepaniak2002/Rooms_booking_system/assets/101816148/ce9ff203-d3f5-40b5-912c-daf83abb5d59)


![Zrzut ekranu 2024-04-26 123346](https://github.com/szczepaniak2002/Rooms_booking_system/assets/101816148/c9d363c1-a2ce-4916-a932-7f932718cf2e)


![Zrzut ekranu 2024-04-26 123532](https://github.com/szczepaniak2002/Rooms_booking_system/assets/101816148/5d04e6fb-bb8d-4d01-809e-25b91a231ade)


![Zrzut ekranu 2024-04-26 123541](https://github.com/szczepaniak2002/Rooms_booking_system/assets/101816148/9cb607ea-5626-492e-b6f7-28fedf01a40a)


![Zrzut ekranu 2024-04-26 123322](https://github.com/szczepaniak2002/Rooms_booking_system/assets/101816148/a0f8145e-3bdb-4fe9-be9b-71d5c368dc1d)


## Uruchomienie 
Najpierw musimy zadbać o pobranie odpowiedniej wersji Django.
Możemy to zrobić używając: 
```bash
pip install -r requirements.txt
```

Następnie należy otworzyć projekt (ja używałem PycharmProfessional). Projekt autmatycznie powinien otworzyć się jako projekt Django.

W konsoli pythona użyj polecenia:
```bash
python manage.py runserver
```
Po uruchomieniu serwera zobaczysz informacje na temat adresu URL, pod którym działa serwer. Domyślnie będzie to `http://127.0.0.1:8000/`.
Otwórz przeglądarkę i wpisz ten adres. Gotowe!!!
