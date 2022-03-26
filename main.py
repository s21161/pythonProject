import csv
import os
import sys
import getpass
import string


def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(current_dir)
    print(os.path.join(current_dir, "db.csv"))
    db_path = os.path.join(current_dir, "db.csv")
    check_db_exists(db_path)


def listowanie():
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        print("Lista użytkowników: ")
        numeracja = 1
        for uzytkownik, haslo in csv_reader:
            print("Użytkownik", numeracja, ": ", uzytkownik)
            numeracja += 1


def sortowanie():
    user_sort_choice = int(input("Wpisz 1 aby posortować użytkowników: "))
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        if user_sort_choice == 1:
            print("Posortowana lista: ")
            nazwy = []
            for uzytkownik, haslo in csv_reader:
                nazwy.append(uzytkownik)
            nazwy.sort()
            numeracja = 1
            for user in nazwy:
                print("Użytkownik", numeracja, ": ", user)
                numeracja += 1

def rejestracja():
    def long_enough(haslo):
        # Przynajmniej 6 znakow
        return len(haslo) >= 6

    def has_uppercase(haslo):
        # Przynajmniej jedna duża litera
        return len(set(string.ascii_uppercase).intersection(haslo)) > 0

    def has_numeric(haslo):
        # Musi zawierać cyfrę
        return len(set(string.digits).intersection(haslo)) > 0

    nazwausera = input("Podaj login: ")
    nazwausera.casefold()
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for nazwy, hasla in csv_reader:
            if nazwausera.casefold() == nazwy.casefold():
                print("Nazwa użytkownika jest już zajęta")
                rejestracja()

    #haslo = input("Podaj hasło: ")
    #haslo2 = input("Ponownie podaj hasło: ")
    haslo = getpass.getpass("Podaj hasło: ")
    haslo2 = getpass.getpass("Ponownie podaj hasło: ")
    if haslo == haslo2 and long_enough(haslo) and has_uppercase(haslo) and has_numeric(
            haslo):
        with open(db_path, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([nazwausera, haslo])
            print("Utworzono użytkownika.")
            exit()
    else:
        print(
            "Podane hasła się nie zgadzają lub hasło jest zbyt mało bezpieczne. \n Rejestrajca:")
        rejestracja()


def logownie():
    uzytkownik = input("Podaj nazwe uzytkonika: ")
    #haslo = input("Podaj hasło: ")
    haslo = getpass.getpass("Podaj hasło: ")
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for nazwy, hasla in csv_reader:
            if uzytkownik.casefold() == nazwy.casefold() and haslo == hasla:
                print("Udało się zalogować!")
                return True
    print("Niepoprawy login lub hasło")
    logownie()
    return False


def usun():
    nowa = []
    uzytkowik_do_usuniecia = input("Podaj nazwe uzytkownika użytkownika do usunięcia: ")
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for wiersz in csv_reader:
            nowa.append(wiersz)
            for field in wiersz:
                if field == uzytkowik_do_usuniecia:
                    nowa.remove(wiersz)
    with open(db_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(nowa)


menu = int(input("1 - LOGOWANIE, 2 - REJESTRACJA: "))

if menu == 1:
    logownie()
    pass
    menu_drugie = int(input("1 - LISTOWANIE UZYTKOWNIKOW, 2 - USUN UZYTKOWNIKA:  "))
    if menu_drugie == 1:
        listowanie()
        sortowanie()

    elif menu_drugie == 2:
        listowanie()
        usun()

elif menu == 2:
    rejestracja()

else:
    pass