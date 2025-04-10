# from models.notes_book import NotesBook

class RecordNote:
    def __init__(self, title, description = "", tags = None):
        self.title = title
        self.description = description
        self.tags = tags if tags else []

    def __str__(self):
        tags = ", ".join(t for t in self.tags)
        return f"title: {self.title} text: {self.description} tags: {tags}"

    def add_note(self, note):
        self.append(note)