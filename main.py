from utils import collections_fun as fn
from utils.parse_input import parse_input
from libs.storage import load_data, save_data
from utils.menu import print_menu

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    command_map = {
        "hello": lambda args: "How can I help you?",
        "add": lambda args: fn.add_contact(args, book),
        "change": lambda args: fn.change_contact(args, book),
        "phone": lambda args: fn.show_phone(args, book),
        "all": lambda args: fn.show_all(args, book),
        "add-birthday": lambda args: fn.add_birthday(args, book),
        "show-birthday": lambda args: fn.show_birthday(args, book),
        "birthdays": lambda args: fn.birthdays(args, book),
    }

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input)

        if command in ("exit", "close"):
            save_data(book)
            print("Good bye!")
            break

        handler = command_map.get(command)
        if handler:
            try:
                result = handler(args)
                if result:  # Якщо функція щось повертає
                    print(result)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    print_menu()
    main()
