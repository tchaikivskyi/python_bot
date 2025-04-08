from decorators.error_handlers import input_error
from models.address_book import AddressBook
from models.record import Record
from utils.input_validate_phone import input_validate_phone
from utils.input_validate_email import input_validate_email
from utils.input_validate_br import input_validate_br

# To move edit_contact_options to another file
edit_contact_options = {
    "1": "Edit Name",
    "2": "Edit Phones",
    "3": "Edit Emails",
    "4": "Edit birthday",
    "5": "Edit address",
}


@input_error
def add_contact(book: AddressBook):
    user_first_name = input("Enter a your first name : ")
    user_last_name = input("Enter a your last name : ")
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
    # You need to add check fun if user exist !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    message = "User is saved"
    print(message)
    return message


@input_error
def change_contact(book: AddressBook):
    user_name_input = input("Enter contact name to edit : ")
    record = book.find(user_name_input)
    if not record:
        return "Contact not found!"
    print()
    print("Edit options")
    print()

    for key, value in edit_contact_options.items():
        print(f"{key} - {value}")

    chose_input = input("Choose what to edit (1-5): ")

    match chose_input:
        case "1":  # Edit Name
            pass
        case "2":  # Edit Phones
            new_phone = input("Give me a new phone:😯 ")
            record.edit_phone(new_phone)
        case "3":  # "Edit Emails",
            pass
        case "4":  # "Edit birthday",
            pass
        case "5":  # "Edit address",
            pass
        case _:
            print("Invalid command!")


# name, old_phone, new_phone = args
# record = book.find(name)
# if not record:
#     return "Contact not found!"

# if record.edit_phone(old_phone, new_phone):
#     return f"Contact {name} updated with new phone!"
# return "Old phone number not found!"


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
    record = book.find(name)
    if not record:
        return "Contact not found!"

    record.add_birthday(birthday_date)
    return f"Birthday for {name} added!"


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found!"

    if not record.birthday:
        return f"No birthday found for {name}"

    return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"


@input_error
def birthdays(_, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays == "No upcoming birthdays.":
        return upcoming_birthdays

    return "\n".join(
        [
            f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')}"
            for record in upcoming_birthdays
        ]
    )

@input_error
def contact_search(args, book: AddressBook):
    pass


@input_error
def contact_show(args, book: AddressBook):
    if not args:
        return "Please provide the name of the contact."

    name = args[0]
    record = book.find(name)

    if not record:
        return "Contact not found!"

    return str(record)