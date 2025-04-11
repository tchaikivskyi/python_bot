# from models.notes_book import NotesBook
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class RecordNote:
    def __init__(self, title, description = "", tags = None):
        self.title = title
        self.description = description
        self.tags = tags if tags else []

    def __str__(self):
        tags = ", ".join(self.tags)
        return f"Title: {self.title} | Text: {self.description} | Tags: {tags}"
    # def __rich__(self):
    #     content = Text()
    #     content.append(f"📄 Text:\n", style="bold cyan")
    #     content.append(f"{self.description}\n\n", style="white")
    #     content.append(f"🏷 Tags: ", style="bold green")
    #     content.append(f"{', '.join(self.tags)}", style="white")

    #     return Panel(
    #         content,
    #         title=f"📝 {self.title}",
    #         title_align="left",
    #         border_style="white",
    #         padding=(1, 2),
    #         expand=False
    #     )
    
    # def show_all(_, note: NotesBook):
    #     if not note.data:
    #         return "Your notes book is empty!"

    #     for record in note.data.values():
    #         console.print(record)
    #     return ""

    def add_note(self, note):
        self.append(note)