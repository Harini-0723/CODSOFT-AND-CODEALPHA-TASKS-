contacts = {}


def add_contact():
    name = input("Enter Name: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n========== CONTACT LIST ==========")

    for name, details in contacts.items():
        print(f"\nName    : {name}")
        print(f"Phone   : {details['Phone']}")
        print(f"Email   : {details['Email']}")
        print(f"Address : {details['Address']}")


def search_contact():
    name = input("Enter contact name to search: ").strip()

    if name in contacts:
        details = contacts[name]
        print("\nContact Found")
        print(f"Name    : {name}")
        print(f"Phone   : {details['Phone']}")
        print(f"Email   : {details['Email']}")
        print(f"Address : {details['Address']}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter New Phone Number: ")
    email = input("Enter New Email: ")
    address = input("Enter New Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():

    while True:

        print("\n==============================")
        print("      CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            search_contact()

        elif choice == '4':
            update_contact()

        elif choice == '5':
            delete_contact()

        elif choice == '6':
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()