from rich.console import Console
from rich.table import Table

console = Console()

def create_table(title, title_style, column_styles, rows):
    table = Table(title=title, title_style=title_style)
    for col, style in column_styles:
        table.add_column(col, style=style)
    for row in rows:
        table.add_row(*row) # розпаковує елементи на масив row == ["add", "Add a new contact"]
    return table

def print_menu():
    menu_sections = [
        {
            "title": "Contact Management",
            "title_style": "bold cyan",
            "column_styles": [("Command", "cyan"), ("Description", "white")],
            "rows": [
                ("contact-add", "Add a new contact"),
                ("test", "Test"),
                ("contact-edit", "Edit a contact"),
                ("contact-show", "Show contact by name"),
                ("contact-all", "Show all contacts"),
                ("contact-search", "Search all contacts by input value"),
                ("contact-delete", "Delete contact by name"),
                ("contact-phone", "Show contact phone by name"),
                ("contact-email", "Show contact email by name"),
                ("contact-address", "Show contact address by name"),
                ("contact-add-birthday", "Add birthday to contact"),
                ("contact-show-birthday", "Show birthday for a contact"),
                ("contact-birthdays", "Show upcoming birthdays"),
            ]
        },
        {
            "title": "Note Management",
            "title_style": "bold red",
            "column_styles": [("Command", "magenta"), ("Description", "white")],
            "rows": [
                ("note-add", "Add a new note"),
                ("note-edit", "Edit a note"),
                ("note-all ", "Show all notes"),
                ("note-search", "Search notes"),
                ("note-add-tag", "Add a tag to a note"),
                ("note-search-by-tag", "Search notes by tag"),
                ("note-sort-by-tag", "Sort notes by tags"),
            ]
        },
        {
            "title": "Other Commands",
            "title_style": "bold green",
            "column_styles": [("Command", "green"), ("Description", "white")],
            "rows": [
                ("hello", "Greet the assistant"),
                ("help", "Show all commands"),
                ("exit / close", "Save data and exit the program"),
            ]
        }
    ]

    for section in menu_sections:
        table = create_table(
            section["title"],
            section["title_style"],
            section["column_styles"],
            section["rows"]
        )
        console.print(table)