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

            name = pet_data.get_name()
            species = pet_data.get_species()
            age = pet_data.get_age()
            weight = pet_data.get_weight()
            onwers_name = pet_data.get_owners_name()
            owners_surname = pet_data.get_owners_surname()

            pets[name] = {
                "Imie": name,
                "Gatunek": species,
                "Wiek": age,
                "Waga": weight,
                "Imie opiekuna": onwers_name,
                "Nazwisko opiekuna": owners_surname
            }

            print("\n")
            print(f"Zarejestrowano zwierzę o imieniu: {name}")
            for key, value in pets[name].items():
                print(f"{key}: {value}")
            with open("Animal_Patient.json", "w") as file:
                json.dump(pets, file, indent=4)

        case Menu.unregister:
            unregister = input("Podaj imie zwierzecia które chcesz wyrejestrować: ").capitalize()
            if unregister in pets:
                del pets[unregister]
                print("Wyrejestrowano zwierze o imieniu: ", unregister)
                with open("Animal_Patient.json", "w") as file:
                    json.dump(pets, file, indent=4)

        case Menu.show:
            for patient in pets:
                print("\n")
                for info in pets[patient]:
                    print(info, pets[patient][info])

        case Menu.search:
            search = input("Podaj imie zwierzęcia: ").capitalize()
            if search in pets:
                print("\n")
                for key, value in pets[search].items():
                    print(f"{key}: {value}")
