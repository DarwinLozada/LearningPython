import pickle
from tkinter import *
from tkinter import ttk
from time import sleep


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


SAVE_FILE_NAME = "contacts.save"


def add_contact(contacts, name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)
    return contact


def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact.name).grid(column=1, row=row, padx="12")
    ttk.Label(frame_contact_list, text=contact.phone).grid(column=2, row=row, padx="10")
    ttk.Label(frame_contact_list, text=contact.email).grid(column=3, row=row, padx="10")


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


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def take_contact_from_contacts(contacts):
    contacts_to_show = []
    for contact in contacts:
        name = contact.name
        phone = contact.phone
        email = contact.email
        contact = Contact(name, phone, email)
        contacts_to_show.append(contact)
    return contacts_to_show


def show_saved_contacts(frame_contact_list, contacts):
    contacts = take_contact_from_contacts(contacts)
    for contact in contacts:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=contact.name).grid(column=1, row=row, padx="12")
        ttk.Label(frame_contact_list, text=contact.phone).grid(column=2, row=row, padx="10")
        ttk.Label(frame_contact_list, text=contact.email).grid(column=3, row=row, padx="10")


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()

    root = Tk()
    root.title("Agenda de contactos")
    frame_add_contact = ttk.Frame(root, padding="30 12 30 12")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="30 12 30 12")
    frame_contact_list.grid()

    name = StringVar()
    phone = StringVar()
    email = StringVar()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Teléfono").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="E-mail").grid(column=3, row=1)

    ttk.Entry(frame_add_contact, width=10, textvariable=name).grid(column=1, row=2, sticky=W, padx="10")
    ttk.Entry(frame_add_contact, width=10, textvariable=phone).grid(column=2, row=2, sticky=W, padx="10")
    ttk.Entry(frame_add_contact, width=10, textvariable=email).grid(column=3, row=2, sticky=W, padx="10")

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1, padx="12")
    ttk.Label(frame_contact_list, text="Teléfono").grid(column=2, row=1, padx="10")
    ttk.Label(frame_contact_list, text="E-mail").grid(column=3, row=1, padx="10")

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3, pady="8")

    ttk.Button(frame_add_contact, text="Guardar contactos", command=lambda: save_contacts(contacts)).grid(column=1,
                                                                                                          row=4,
                                                                                                          pady="8")
    show_saved_contacts(frame_contact_list, contacts)

    root.mainloop()


if __name__ == "__main__":
    main()
