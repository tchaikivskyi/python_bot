from utils import collections_fun as fn, notes_fun
from utils.menu import print_menu
from libs.storage import load_data, save_data


def main():
    book, note = load_data().values()
    print("Welcome to the assistant bot!")

    command_map = {
        "hello": lambda *args: print("How can I help you?"),
        "help": lambda *args: print_menu(),
        # "contact add": lambda args: fn.add_contact(book),
        "add": lambda args: fn.add_contact(book),
        # "contact edit": lambda args: fn.change_contact(book),
        "edit": lambda args: fn.change_contact(book),
        # "contact show": lambda args: fn.contact_show(args, book),
        "show": lambda args: fn.contact_show(book),
        # "contact all": lambda args: fn.show_all(args, book),
        "all": lambda args: fn.show_all(args, book),
        "contact search": lambda args: fn.contact_search(args, book),
        "contact delete": lambda args: print("contact delete"),
        "contact phone": lambda args: fn.show_phone(args, book),
        "contact email": lambda args: print("contact email"),
        "contact address": lambda args: print("contact address"),
        "contact add-birthday": lambda args: fn.add_birthday(args, book),
        "contact show-birthday": lambda args: fn.show_birthday(args, book),
        "contact birthdays": lambda args: fn.birthdays(args, book),
        "note add": lambda args: notes_fun.add_note(note),
        "note edit": lambda args: print("note edit"),
        "note all": lambda args: notes_fun.show_all(args, note),
        "note search": lambda args: print("note search"),
        "note add-tag": lambda args: print("note add-tag"),
        "note search-by-tag": lambda args: print("note search-by-tag"),
        "note sort-by-tag": lambda args: print("note sort-by-tag"),
    }

    while True:
        user_input = input("Enter a command: ").strip().lower()

        if not user_input:
            print("Invalid command.")
            continue

        parts = user_input.split()
        cmd = (
            " ".join(parts[:2])
            if len(parts) >= 2 and " ".join(parts[:2]) in command_map
            else parts[0]
        )
        args = parts[2:] if cmd in command_map and len(parts) > 2 else parts[1:]

        if cmd in command_map:
            handler = command_map[cmd]
            try:
                result = handler(args)
                if result:
                    print(result)
            except Exception as e:
                print(f"Error: {e}")
        elif user_input in ("exit", "close"):
            save_data({"book": book, "note": note})
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    print_menu()
    main()
