import json
import os

CONTACTS_FILE = "contacts.json"

# -------------------- File Handling --------------------
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# -------------------- Core Functions --------------------
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
        print()


def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("Enter contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            contacts[idx]["phone"] = input("Enter new phone: ")
            contacts[idx]["email"] = input("Enter new email: ")
            save_contacts(contacts)
            print("✅ Contact updated successfully!\n")
        else:
            print("❌ Invalid selection.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            save_contacts(contacts)
            print(f"✅ Contact '{removed['name']}' deleted successfully!\n")
        else:
            print("❌ Invalid selection.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")


# -------------------- Main Program --------------------
def main():
    contacts = load_contacts()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
