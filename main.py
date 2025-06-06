from utils import collections_fun as fn, notes_fun
from utils.menu import print_menu
from utils.storage import load_data, save_data
from utils.colored_text import colored_input, colored_text
from utils.input_hinter import suggest_commands 
from utils.add_test_data import add_test_data


def main():
    book, note = load_data().values()

    command_map = {
        "hello": lambda *args: colored_text("How can I help you?"),
        "help": lambda *args: print_menu(),
        "test data": lambda *args: add_test_data(book, note),
        "contact add": lambda args: fn.add_contact(book),
        "contact edit": lambda args: fn.change_contact(book),
        "contact show": lambda args: fn.contact_show(book),
        "contact all": lambda args: fn.show_all(book),
        "contact search": lambda args: fn.contact_search(book),
        "contact delete": lambda args: fn.delete_contact(book),
        "contact birthdays": lambda args: fn.show_up_birthdays(book),
        "note add": lambda args: notes_fun.add_note(note),
        "note edit": lambda args: notes_fun.edit_note(note),
        "note all": lambda args: notes_fun.show_all(args, note),
        "note search": lambda args: notes_fun.search_note_by_title(note),
        "note search-by-tag": lambda args: notes_fun.search_by_tag(args, note),
        "note sort-by-tag": lambda args: notes_fun.sort_by_tags(args, note),
        "note delete": lambda args: notes_fun.delete_note(note),
    }

    while True:
        user_input = colored_input("Enter a command", "blue").strip().lower()

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
                colored_text(f"Error: {e}", "red")
        elif user_input in ("exit", "close"):
            save_data({"book": book, "note": note})
            colored_text("Good bye!")
            break
        else:
            suggestions = suggest_commands(user_input, command_map)
            if suggestions:
                colored_text("Did you mean one of these?", "yellow")
                for suggestion in suggestions:
                    colored_text(f" - {suggestion}", "yellow")
            else:
                colored_text("Invalid command.", "red")


if __name__ == "__main__":
    colored_text("Welcome to the assistant bot!")
    print_menu()
    main()
