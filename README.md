# Portal z ogłoszeniami UKR-INFO

## ToDo
- [x] System logowania oraz rejestracji - potrzebne dane: nazwa użytkownika, adres e-mail oraz hasło.
- [x] System edycji profilu użytkownika - użytkownik może edytować nazwę użytkownika oraz e-mail.
- [x] System dodawania ogłoszeń - potrzebne dane: tytuł, opis, kategoria, typ - informacje o autorze oraz dacie wczytywane są automatycznie.
- [x] System edytowania ogłoszeń 

## Wykorzystane technologie
- Django 3.0.14 
- Python 3.10.4 
- Flowbite 1.4.7 (UI Kit)

## Przed instalacją
Upewnić się czy posiadamy zainstalowane na komputerze:
 - Python w wersji 3.10.4 lub wyżej
 - PIP w wersji 22.1.1 lub wyzej
 
 Na starszych wersjach mogą wystąpić problemy z instalacją wymaganych pakietów z `requirements.txt`

## Uruchomienie lokalne
1. Instalacja potrzebnych pakietów
```
pip install requirements.txt 
```

2. Uruchomienie projektu
```
python manage.py runserver
```

## Wygląd i funkcjonalność

1. Strona główna:
![127 0 0 1_8000](https://user-images.githubusercontent.com/40581509/176994915-e1dd30ba-57c1-4725-b46c-b9ca9adbabc2.png)

2. Logowanie
![127 0 0 1_8000_login](https://user-images.githubusercontent.com/40581509/176994921-90f09ffb-b83a-4de9-97c0-3ff08563db60.png)

3. Rejestracja
![register2](https://user-images.githubusercontent.com/40581509/176995003-79717c6f-606b-41de-a776-4bf36360fb01.png)


4. Edycja ogłoszenia - z uprawnieniami:
![127 0 0 1_8000_edit](https://user-images.githubusercontent.com/40581509/176994927-acf43b1c-018a-4f48-97e2-c9fb5a53a1d1.png)


5. Edycja ogłoszenia - bez uprawnień:
![127 0 0 1_8000](https://user-images.githubusercontent.com/40581509/176994915-e1dd30ba-57c1-4725-b46c-b9ca9adbabc2.png)

6. Dodanie ogłoszenia
![127 0 0 1_8000_dodaj](https://user-images.githubusercontent.com/40581509/176994942-00cc1bbc-e80b-419a-a576-bfa14f43b72b.png)

7. Profil
![127 0 0 1_8000_profile](https://user-images.githubusercontent.com/40581509/176994959-c1f38470-7146-48ff-a7d4-660f7978af38.png)






## Live demo
W budowie...
