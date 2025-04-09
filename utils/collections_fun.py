from datetime import datetime
from decorators.error_handlers import input_error
from models.address_book import AddressBook
from models.record import Record
from utils.input_validate_phone import input_validate_phone
from utils.input_validate_email import input_validate_email
from utils.input_validate_br import input_validate_br


@input_error
def add_contact(book: AddressBook):
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    full_name = f"{user_first_name} {user_last_name}"

    if book.find_by_full_name(full_name):
        return f"Contact '{full_name}' already exists!"

    user_email = input_validate_email()
    user_phones = input_validate_phone()
    user_br = input_validate_br()

    new_user = {
        "first_name": user_first_name,
        "last_name": user_last_name,
        "email": user_email,
        "phones": user_phones,
        "birthday_date": user_br,
    }

    record = Record(**new_user)
    book.add_record(record)

    return "User is saved"


@input_error
def change_contact(book: AddressBook):
    full_name_input = input("Enter contact full name to edit (First Last): ").strip()
    record = book.find_by_full_name(full_name_input)

    if not record:
        print("Contact not found!")
        return

    print("\nEdit options\n")
    print("1 - Edit Name")
    print("2 - Edit Phones")
    print("3 - Edit Emails")
    print("4 - Edit birthday")
    print("5 - Edit address")
    print("6 - Edit remove contact\n")

    choice = input("Choose what to edit (1-5): ").strip()

    match choice:
        case "1":  # Edit Name
            old_key = f"{record.first_name.value} {record.last_name.value}"
            new_first = input("Enter a new first name: ").strip()
            new_last = input("Enter a new last name: ").strip()
            record.change_name(new_first, new_last)
            new_key = f"{record.first_name.value} {record.last_name.value}"

            if old_key != new_key:
                book.data.pop(old_key)
                book.data[new_key] = record

            print("Name updated successfully.")

        case "2":  # Edit Phones
            print("Current phones:")
            for p in record.phones:
                print(f"- {p}")

            print("\nEdit phone options")
            print("1 - Add new phone")
            print("2 - Edit phone")
            print("3 - Delete\n")

            action = input("Choose action: (1-3): ").strip()

            if action == "1":
                new_phone = input_validate_phone()
                record.add_phone(new_phone)
                print("Phone added.")
            elif action == "2":
                old_phone = input("Enter the old phone to replace: ").strip()
                new_phone = input_validate_phone("Enter the new phone: ")
                if record.edit_phone(old_phone, new_phone):
                    print("Phone updated.")
                else:
                    print("Old phone not found.")
            elif action == "3":
                phone_to_remove = input("Enter the phone to delete: ").strip()
                if record.remove_phone(phone_to_remove):
                    print("Phone deleted.")
                else:
                    print("Phone not found.")
            else:
                print("Invalid phone action.")

        case "3":  # Edit Email
            new_email = input_validate_email("Enter a new email: ")
            record.change_email(new_email)
            print("Email updated.")

        case "4":  # Edit Birthday
            print(f"\nYour current birthday date is - {record.birthday}\n")
            new_birthday = input_validate_br("Enter a new birthday (DD.MM.YYYY): ")
            record.add_birthday(new_birthday)
            print("Birthday updated.")

        case "5":  # Edit Address
            new_address = input("Enter a new address: ").strip()
            record.change_address(new_address)
            print("Address updated.")
        case "6":  # Remove
            current_user_name = record.get_full_name()
            print(f"\nCurrent user full name = {current_user_name}\n")
            ask_input = (
                input("Are you sure that yo want to remove contact ?: (Y|N)  ")
                .lower()
                .strip()
            )
            if ask_input == "y":
                book.delete(current_user_name)
                print(f"Contact with name {current_user_name} is deleted successfully ")
            elif ask_input == "n":
                return
            else:
                print("Invalid answer command!")

        case _:
            print("Invalid command!")


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found!"

    phones = [p.value for p in record.phones]
    return (
        f"Phone(s) for {name}: {', '.join(phones)}"
        if phones
        else "No phone number found!"
    )


@input_error
def show_all(_, book: AddressBook):
    if not book.data:
        return "Your address book is empty!"

    return "\n".join([str(record) for record in book.data.values()])


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Please use format: add-birthday <name> <DD.MM.YYYY>"

    name, birthday_date = args
    record = book.find_by_full_name(name)
    if not record:
        return "Contact not found!"

    record.add_birthday(birthday_date)
    return f"Birthday for {name} added!"


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find_by_full_name(name)
    if not record:
        return "Contact not found!"

    if not record.birthday:
        return f"No birthday found for {name}"

    return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"


@input_error
def birthdays(_, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."

    return "\n".join(
        [
            f"{record.first_name.value} {record.last_name.value}: {record.birthday.value.strftime('%d.%m.%Y')}"
            for record in upcoming_birthdays
        ]
    )


@input_error
def contact_search(args, book: AddressBook):
    pass


@input_error
def contact_show(book: AddressBook):

    full_name_input = (
        input("Enter contact full name to show you (First Last): ").strip().lower()
    )

    record = book.find_by_full_name(full_name_input)

    if not record:
        return "Contact not found! Try again"

    return record
