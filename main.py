from utils import collections_fun as fn, notes_fun
from utils.menu import print_menu
from utils.storage import load_data, save_data
from utils.colored_text import colored_input, colored_text

def main():
    book, note = load_data().values()

    command_map = {
        "hello": lambda *args: colored_text("How can I help you?"),
        "help": lambda *args: print_menu(),
        "contact add": lambda args: fn.add_contact(book),
        "contact edit": lambda args: fn.change_contact(book),
        "contact show": lambda args: fn.contact_show(book),
        "contact all": lambda args: fn.show_all(book),
        "contact search": lambda args: fn.contact_search(args, book),
        "contact delete": lambda args: print("contact delete"),
        "contact phone": lambda args: fn.show_phone(args, book),
        "contact email": lambda args: print("contact email"),
        "contact address": lambda args: print("contact address"),
        "contact add-birthday": lambda args: fn.add_birthday(args, book),
        "contact show-birthday": lambda args: fn.show_up_birthdays(args, book),
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
        user_input = colored_input("Enter a command: ", "blue").strip().lower()

        if not user_input:
            colored_text("Invalid command.", "red")
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
                    colored_text(result)
            except Exception as e:
                colored_text(f"Error: {e}")
        elif user_input in ("exit", "close"):
            save_data({"book": book, "note": note})
            colored_text("Good bye!")
            break
        else:
            colored_text("Invalid command.", "red")


if __name__ == "__main__":
    colored_text("Welcome to the assistant bot!")
    print_menu()
    main()
