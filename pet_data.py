def get_choise():
    while True:
        choise_str = input("Wybierz działanie: ")
        try:
            choise = int(choise_str)
            return choise
        except ValueError:
            print("Błąd: Wybierz działanie menu 1-4: ")


def get_name():
    while True:
        name = input("Podaj imie zwierzecia: ").capitalize()
        return name


def get_species():
    while True:
        species = input("Podaj gatunek zwierzęcia: ").capitalize()
        return species


def get_weight():
    while True:
        weight_str = input("Podaj wagę zwierzęcia: ")
        weight_str = weight_str.replace(',', '.')
        try:
            weight = float(weight_str)
            return weight
        except ValueError:
            print("Błąd: Podaj poprawną wage używając tylko liczb.")


def get_age():
    while True:
        age_str = input("Podaj wiek zwierzęcia: ")
        try:
            age = int(age_str)
            return age
        except ValueError:
            print("Błąd: Podaj poprawny wiek używając tylko liczb.")


def get_owners_name():
    while True:
        owners_name = input("Podaj imie właściciela: ").capitalize()
        return owners_name


def get_owners_surname():
    while True:
        owners_surname = input("Podaj nazwisko właściciela: ").capitalize()
        return owners_surname
