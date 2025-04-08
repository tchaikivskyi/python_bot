from decorators.error_handlers import input_error
from models.notes_book import NotesBook
from models.record_note import RecordNote


@input_error
def add_note(note: NotesBook):
    print("Funcion create note\n")
    title = input("Enter title : ")


    record = RecordNote(title)
    note.add_record(record)

    message = "Note is saved"
    print(message)
    return message


@input_error
def show_all(_, note: NotesBook):
    if not note.data:
        return "Your notes book is empty!"

    return "\n".join([str(record) for record in note.data.values()])