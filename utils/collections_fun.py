from decorators.error_handlers import input_error
from models.address_book import AddressBook
from models.record import Record
from utils.input_validate import (
    input_validate_phone,
    input_validate_email,
    input_validate_br,
    input_validate_field,
)
from utils.table import dynamic_table
from utils.parse_to_dict import parse_data_str_to_dict
from utils.colored_text import colored_input, colored_text


@input_error
def add_contact(book: AddressBook):
    user_first_name = input_validate_field(
        "Enter your first name", length=2, field_type="name"
    )
    user_last_name = input_validate_field(
        "Enter your last name", length=2, field_type="name"
    )
    full_name = f"{user_first_name} {user_last_name}"

    if book.find_by_full_name(full_name):
        return f"Contact '{full_name}' already exists!"

    user_email = input_validate_email()
    user_phones = input_validate_phone()
    user_br = input_validate_br()
    user_address = input_validate_field("Enter your address", length=3)

    new_user = {
        "first_name": user_first_name,
        "last_name": user_last_name,
        "email": user_email,
        "phones": user_phones,
        "birthday_date": user_br,
        "address": user_address,
    }

    record = Record(**new_user)
    book.add_record(record)

    return colored_text("User is saved")


@input_error
def change_contact(book: AddressBook):
    full_name_input = colored_input(
        "Enter contact full name to edit (First Last)"
    ).strip()
    record = book.find_by_full_name(full_name_input)

    if not record:
        colored_text("Contact not found!", "yellow")
        return

    colored_text("\nEdit options\n")
    colored_text("1 - Edit Name", "cyan")
    colored_text("2 - Edit Phones", "cyan")
    colored_text("3 - Edit Emails", "cyan")
    colored_text("4 - Edit birthday", "cyan")
    colored_text("5 - Edit address\n", "cyan")

    choice = colored_input("Choose what to edit (1-5)").strip()

    match choice:
        case "1":  # Edit Name
            old_key = f"{record.first_name.value} {record.last_name.value}"
            new_first = colored_input("Enter a new first name", "cyan").strip()
            new_last = colored_input("Enter a new last name", "cyan").strip()
            record.change_name(new_first, new_last)
            new_key = f"{record.first_name.value} {record.last_name.value}"

            if old_key != new_key:
                book.data.pop(old_key)
                book.data[new_key] = record

            colored_text("Name updated successfully.")

        case "2":  # Edit Phones
            colored_text("Current phones:")
            for p in record.phones:
                colored_text(f"- {p}", "cyan")

            colored_text("\nEdit phone options")
            colored_text("1 - Add new phone", "cyan")
            colored_text("2 - Edit phone", "cyan")
            colored_text("3 - Delete\n", "cyan")

            action = colored_input("Choose action: (1-3)").strip()

            if action == "1":
                new_phone = input_validate_phone()
                record.add_phone(new_phone)
                colored_text("Phone added.")

            elif action == "2":
                old_phone = colored_input(
                    "Enter the old phone to replace", "cyan"
                ).strip()
                new_phone = input_validate_phone("Enter the new phone")
                if record.edit_phone(old_phone, new_phone):
                    colored_text("Phone updated.")
                else:
                    colored_text("Old phone not found.", "yellow")

            elif action == "3":
                phone_to_remove = colored_input(
                    "Enter the phone to delete", "cyan"
                ).strip()
                if record.remove_phone(phone_to_remove):
                    colored_text("Phone deleted.")
                else:
                    colored_text("Phone not found.", "yellow")
            else:
                colored_text("Invalid phone action.", "red")

        case "3":  # Edit Email
            new_email = input_validate_email("Enter a new email")
            record.change_email(new_email)
            colored_text("Email updated.")

        case "4":  # Edit Birthday
            # colored_text(
            #     f"\nYour current birthday date is - {record.birthday}\n", "cyan"
            # )
            new_birthday = input_validate_br("Enter a new birthday (DD.MM.YYYY)")
            record.add_birthday(new_birthday)
            colored_text("Birthday updated.")

        case "5":  # Edit Address
            new_address = input_validate_field("Enter a new address", length=3).strip()
            record.change_address(new_address)
            colored_text("Address updated.")
        case _:
            colored_text("Invalid command!", "red")


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "Your address book is empty!"

    contacts_list = []
    for record in book.data.values():
        contact_dict = parse_data_str_to_dict(str(record))
        contacts_list.append(contact_dict)

    dynamic_table(title="All contacts", rows=contacts_list, style="cyan")


@input_error
def show_up_birthdays(book: AddressBook):
    days_input = colored_input(
        "Enter the number of days to check upcoming birthdays (default is 7)"
    )

    if not days_input:
        days_input = 7

    upcoming_birthdays = book.get_upcoming_birthdays(days=int(days_input))

    if not upcoming_birthdays:
        return colored_text("No upcoming birthdays.", "yellow")

    birthday_rows = [
        {
            "Contact name": f"{record.first_name.value.title()} {record.last_name.value.title()}",
            "Birthday": record.birthday.value.strftime("%d.%m.%Y"),
        }
        for record in upcoming_birthdays
    ]

    dynamic_table(title="Upcoming birthdays", rows=birthday_rows, style="cyan")



@input_error
def contact_show(
    book: AddressBook,
):
    full_name_input = (
        colored_input("Enter contact full name to show you (First Last)", "cyan")
        .strip()
        .lower()
    )

    record = book.find_by_full_name(full_name_input)

    if not record:
        return colored_text("Contact not found!", "yellow")
    
    dynamic_table(title=f"Contact {full_name_input} details", rows=parse_data_str_to_dict(str(record)), style="cyan")

@input_error
def contact_search(book: AddressBook):
    input_query = colored_input(
        "Enter a search word or date of birth in DD.MM.YYYY format: ", "cyan"
    ).strip()

    if not input_query:
        colored_text(
            "Query cannot be empty.",
            "yellow",
        )
        return

    results = book.find_by_query_field(input_query)

    if not results:
        colored_text("No matching contacts found.", "yellow")
        return

    dynamic_table(
        title="Search Results",
        rows=parse_data_str_to_dict("\n".join(str(record) for record in results)),
        style="cyan"
    )

@input_error
def delete_contact(book: AddressBook):
    full_name_input = colored_input(
        "Enter contact full name to remove from address book (First Last)"
    ).strip()

    record = book.find_by_full_name(full_name_input)

    if not record:
        colored_text("Contact not found!", "yellow")
        return

    current_user_name = record.get_full_name()

    colored_text(
        f"\nCurrent user full name = {current_user_name}\n", "cyan"
    )  # Change Please!!! You have to show the table of user data

    ask_input = (
        colored_input("Are you sure that yo want to remove contact ? (Y|N)")
        .lower()
        .strip()
    )

    if ask_input == "y":
        deleted_book = book.delete(current_user_name)
        colored_text(f"Contact with name {current_user_name} is deleted successfully ")
        
        if not record:
            return colored_text("Contact not found!", "yellow")
        
        dynamic_table(title=f"Contact {full_name_input} was deleted", rows=parse_data_str_to_dict(str(deleted_book)), style="cyan")
        
    elif ask_input == "n":
        return
    else:
        colored_text("Invalid answer command!", "red")
