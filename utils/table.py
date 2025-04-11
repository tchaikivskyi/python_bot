from rich.console import Console
from rich.table import Table

__console__ = Console()

def create_table(title, rows = [], style = 'green'):
    table = Table(title=title, title_style=f"bold {style}")
    for col, style in [("Command", style), ("Description", "white")]:
        table.add_column(col, style=style)
    for row in rows:
        table.add_row(*row) # розпаковує елементи на масив row == ["add", "Add a new contact"]
    __console__.print()  # Відступ зверху
    __console__.print(table)
    __console__.print()  # Відступ знизу
    return table

def dynamic_table(title, rows, style='green', column_order=None):
    if isinstance(rows, dict):
        rows = [rows]
    if isinstance(rows, str):
        __console__.print("[red]Expected dict or list of dicts, but got string.[/red]")
        return
    if not rows:
        __console__.print("[yellow]No data to display.[/yellow]")
        return

    if column_order:
        all_keys = column_order 
    else:
        all_keys = list(rows[0].keys()) if rows else []

    table = Table(title=title, title_style=f"bold {style}")
    for key in all_keys:
        table.add_column(key, style="white")

    for contact in rows:
        row = [str(contact.get(key, "")) for key in all_keys]
        table.add_row(*row)

    __console__.print()  # Відступ зверху
    __console__.print(table)
    __console__.print()  # Відступ знизу
    return table

