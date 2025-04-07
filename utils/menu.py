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
                ("add", "Add a new contact"),
                ("change", "Edit a contact"),
                ("phone", "Show contact phone by name"),
                ("all", "Show all contacts"),
                ("add-birthday", "Add birthday to contact"),
                ("show-birthday", "Show birthday for a contact"),
                ("birthdays", "Show upcoming birthdays"),
            ]
        },
        # {
        #     "title": "Note Management",
        #     "title_style": "bold red",
        #     "column_styles": [("Command", "magenta"), ("Description", "white")],
        #     "rows": [
        #         ("add note", "Add a new note"),
        #         ("show all notes", "Show all notes"),
        #         ("search notes", "Search notes"),
        #         ("edit note", "Edit a note"),
        #     ]
        # },
        # {
        #     "title": "Other Commands",
        #     "title_style": "bold green",
        #     "column_styles": [("Command", "green"), ("Description", "white")],
        #     "rows": [
        #         ("hello", "Greet the assistant"),
        #         ("exit / close", "Save data and exit the program"),
        #     ]
        # }
    ]

    for section in menu_sections:
        table = create_table(
            section["title"],
            section["title_style"],
            section["column_styles"],
            section["rows"]
        )
        console.print(table)