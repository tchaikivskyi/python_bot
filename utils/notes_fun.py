from decorators.error_handlers import input_error
from models.notes_book import NotesBook
from models.record_note import RecordNote
from rich.console import Console

console = Console()

@input_error
def add_note(note: NotesBook):
    print("Funcion create note\n")
    title = input("Enter title: ")
    description = input("Enter text: ")
    tags = input("Enter tags separated by commas: ")
    tags = [tag.strip() for tag in tags.split(",")] if tags else []

    new_note = {
        "title": title,
        "description": description,
        "tags": tags
    }

    record = RecordNote(**new_note)
    note.add_record(record)

    message = "Note is saved"
    print(message)
    return message


@input_error
def show_all(_, note: NotesBook):
    if not note.data:
        return "Your notes book is empty!"
    
    for record in note.data.values():
        console.print(record) 
    return ""
    
    # return "\n".join([str(record) for record in note.data.values()])

@input_error
def search_by_tag(_, note: NotesBook):
    tag_to_search = input("Enter the tag to search for: ").strip()

    if not tag_to_search:
        return "Tag cannot be empty."

    matching_notes = [
        record for record in note.data.values() if tag_to_search in record.tags
    ]
    
    if not matching_notes:
        return f"No notes found with the tag '{tag_to_search}'."
    
    # for record in matching_notes:
    #     print(f"Title: {record.title}")
    #     print(f"Text: {record.description}")
    #     print(f"Tags: {', '.join(record.tags)}\n")
    # return ""
    for record in matching_notes:
        console.print(record)  
    return ""



@input_error
def sort_by_tags(_, note: NotesBook):
    if not note.data:
        return "Your notes book is empty!"

    sorted_notes = sorted(note.data.values(), key=lambda record: record.tags[0] if record.tags else "")

    # for record in sorted_notes:
    #     print(f"Title: {record.title}")
    #     print(f"Text: {record.description}")
    #     print(f"Tags: {', '.join(record.tags)}\n")
    # return ""

    # return "\n".join([str(record) for record in sorted_notes])

    for record in sorted_notes:
        console.print(record)  
    return ""