from utils.table import create_table

def print_menu():
    menu_sections = [
        {
            "title": "Contact Management",
            "style": "cyan",
            "rows": [
                ("contact add", "Add a new contact"),
                ("contact edit", "Edit a contact"),
                ("contact show", "Show contact by name"),
                ("contact all", "Show all contacts"),
                ("contact search", "Search all contacts by input value"),
                ("contact delete", "Delete contact by name"),
                ("contact birthdays", "Show upcoming birthdays"),
            ]
        },
        {
            "title": "Note Management",
            "style": "green",
            "rows": [
                ("note add", "Add a new note"),
                ("note edit", "Edit a note"),
                ("note all ", "Show all notes"),
                ("note search", "Search notes by title"),
                ("note search-by-tag", "Search notes by tag"),
                ("note sort-by-tag", "Sort notes by tags"),
                ("note delete", "Delete note"),
            ]
        },
        {
            "title": "Other Commands",
            "style": "red",
            "rows": [
                ("hello", "Greet the assistant"),
                ("help", "Show all commands"),
                ("exit / close", "Save data and exit the program"),
            ]
        }
    ]

    for section in menu_sections:
        create_table(
            title=section["title"],
            style=section["style"],
            rows=section["rows"]
        )
        