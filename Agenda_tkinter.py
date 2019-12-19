import pickle
from tkinter import *
from tkinter import ttk
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_SHOW_CONTACTS = 5
ACTION_EXIT = 6

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT,
                ACTION_SHOW_CONTACTS]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Mostrar los contactos")
    print("6 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    return contact


def remove_contact(contacts):
    sleep(1)
    list_name_contacts = []
    digit_list = []
    name_digit = 0
    for contact in contacts:
        name_contact = contact['name']
        list_name_contacts.append(name_contact)

    print("\n\nEliminar contacto\n")
    sleep(1)
    print("\n¿Qué contacto quieres eliminar?\n")
    sleep(2)

    for contact_name in list_name_contacts:
        print("{}-{}".format(name_digit, contact_name))
        digit_list.append(name_digit)
        name_digit += 1
    digit_contact_eliminate = int(input("Diga el número del contacto que desea eliminar "))
    for digit in digit_list:
        if digit_contact_eliminate == digit:
            contacts.pop(digit_contact_eliminate)
    sleep(2)


def find_contact(contacts):
    print("\nBuscar contacto\n")
    sleep(2)
    search_term_name = input("Introduce el nombre del contacto o parte de él: ")
    search_term_email = input("Introduce el correo del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term_name) >= 0:
            found_contacts.append(contact)
            print("Según el nombre")
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    for contact in contacts:
        if contact["email"].find(search_term_email) >= 0:
            if contact in found_contacts:
                pass
            else:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact["name"]))
                contact_indexes.append(contact_counter)
                contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        user_answer = input("¿Deseas regresar al menú (1) o volver a intentar (2)? ")
        if user_answer == "1":
            return
        elif user_answer == "2":
            find_contact(contacts)

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def show_contacts(contacts):
    print("\nEstos son los contactos")
    contact_counter = 0
    sleep(2)
    for contact in contacts:
        print("{}-Nombre: {name}, Telefono: {phone}, Email: {email}\n".format(contact_counter, **contact))
        contact_counter += 1
        sleep(1)
    sleep(2)
    return


def main():
    contacts = load_contacts()


if __name__ == "__main__":
    main()