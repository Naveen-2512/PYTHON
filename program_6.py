def add_contact(contacts, name, phone, email):
    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def search_contact(contacts, name):
    if name in contacts:
        print("\nContact Found")
        print("Name :", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("Phonebook is empty.")
        return

    print("\n===== ALL CONTACTS =====")

    # Using keys(), values() and items()
    print("\nContact Names:")
    for name in contacts.keys():
        print(name)

    print("\nContact Details:")
    for details in contacts.values():
        print(details)

    print("\nComplete Records:")
    for name, details in contacts.items():
        print(name, "->", details)


def find_names_by_phone(contacts, phone):
    # List comprehension
    names = [
        name for name, details in contacts.items()
        if details["phone"] == phone
    ]

    return names


def main():
    contacts = {}

    while True:
        print("\n===== PHONEBOOK MANAGER =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Search by Phone Number")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            add_contact(contacts, name, phone, email)

        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(contacts, name)

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            update_contact(contacts, name, phone, email)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)

        elif choice == "5":
            display_contacts(contacts)

        elif choice == "6":
            phone = input("Enter phone number: ")

            names = find_names_by_phone(contacts, phone)

            if names:
                print("Matching contacts:", names)
            else:
                print("No contact found.")

        elif choice == "7":
            print("Exiting Phonebook...")
            break

        else:
            print("Invalid choice. Try again.")


main()