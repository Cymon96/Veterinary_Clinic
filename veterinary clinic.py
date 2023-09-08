from enum import IntEnum
import pet_data
import json


class Menu(IntEnum):
    register = 1
    unregister = 2
    show = 3
    search = 4


try:
    with open("Animal_Patient.json", "r") as file:
        pets = json.load(file)
except FileNotFoundError:
    pets = {}

while True:
    print("\n")
    print("Menu weterynarii 'Pod martwym kotkiem'")
    print("1 - Zarejestruj pacjenta\n2 - Wyrejestruj pacjenta\n3 - "
          "Wyświetl wszystkich zarejestrowanych pacjentów\n4 - Znajdź w bazie pacjenta")

    choice = pet_data.get_choise()
    action = Menu(choice)

    match action:
        case Menu.register:
            print("\n")

            key = pet_data.key_generator(pets)
            name = pet_data.get_name()
            species = pet_data.get_species()
            age = pet_data.get_age()
            weight = pet_data.get_weight()
            onwers_name = pet_data.get_owners_name()
            owners_surname = pet_data.get_owners_surname()

            pets[key] = {
                "ID": key,
                "Imie": name,
                "Gatunek": species,
                "Wiek": age,
                "Waga": weight,
                "Imie opiekuna": onwers_name,
                "Nazwisko opiekuna": owners_surname
            }

            print("\n")
            print(f"Zarejestrowano zwierzę o imieniu: {name} ID: {key}")
            for number, value in pets[key].items():
                print(f"{number}: {value}")
            with open("Animal_Patient.json", "w") as file:
                json.dump(pets, file, indent=4)

        case Menu.unregister:
            unregister = input("Podaj numer ID zwierzecia które chcesz wyrejestrować: ")
            if unregister in pets:
                pet = pets[unregister]
                del pets[unregister]
                print(f"Wyrejestrowano zwierzę o imieniu: {pet['Imie']} z numerem ID: {unregister}")
                with open("Animal_Patient.json", "w") as file:
                    json.dump(pets, file, indent=4)
            else:
                print(f"Nie znaleziono zwierzęcia z numerem ID: {unregister}")

        case Menu.show:
            for patient in pets:
                print("\n")
                for info in pets[patient]:
                    print(info, pets[patient][info])

        case Menu.search:
            search = input("Podaj numer ID zwierzęcia: ")
            if search in pets:
                print("\n")
                for key, value in pets[search].items():
                    print(f"{key}: {value}")
