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

# Function search notes by title
@input_error
def search_note_by_title(note: NotesBook):
    # Ask for the note's title to search and ensure it's not empty
    while True:
        query = input("Enter Note's Title: ").strip().lower()
        if query:
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")
    
    results = [record for record in note.data.values() if query in record.title.lower()]

    if not results:
        print(f"No notes found with title '{query}'.")

    return "\n".join([str(record) for record in results])

# Function edit note
@input_error
def edit_note(note: NotesBook):
    # Step 1: Ask for the note's title to be edited and ensure it's not empty
    while True:
        title_to_edit = input("Enter Note's Title to be edited: ").strip().lower()
        if title_to_edit:
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")

    # Step 2: Search for the note by title
    results = [record for record in note.data.values() if title_to_edit in record.title.lower() == title_to_edit]

    if not results:
        return f"No notes found with title containing '{title_to_edit}'."

    # Step 3: Show the found notes
    print("Found the following notes:")
    print("\n".join([str(record) for record in results]))

    #Step 4: Allow user to edit the title, description, and tags
    note_to_edit = results[0]

    new_title = input(f"Enter new title (current: '{note_to_edit.title}') or press Enter to keep it: ").strip()
    new_description = input(f"Enter new description (current: '{note_to_edit.description}') or press Enter to keep it: ").strip()
    new_tags = input(f"Enter new tags separated by commas (current: {', '.join(note_to_edit.tags)}) or press Enter to keep them: ").strip()

    # Check if any field has changed and update accordingly
    changes_made = False

    if new_title and new_title != note_to_edit.title:
        note_to_edit.title = new_title
        changes_made = True

    if new_description and new_description != note_to_edit.description:
        note_to_edit.description = new_description
        changes_made = True

    if new_tags and new_tags != ', '.join(note_to_edit.tags):
        note_to_edit.tags = [tag.strip() for tag in new_tags.split(",")]
        changes_made = True

    # Only update the note in the data if any change has been made
    if changes_made:
        note.data[note_to_edit.title] = note_to_edit
        return f"Note '{note_to_edit.title}' has been updated!"
    else:
        return "No changes made to the note."
    
# Function delete note
@input_error
def delete_note(note: NotesBook):
    # Step 1: Ask for the note's title to be deleted and ensure it's not empty
    while True:
        title_to_delete = input("Enter Note's Title to be deleted: ").strip().lower()
        if title_to_delete:
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")

    # Step 2: Search for the note by title
    results = [record for record in note.data.values() if title_to_delete in record.title.lower() == title_to_delete]

    if not results:
        return f"No notes found with title containing '{title_to_delete}'."

    # Step 3: Show the found notes
    print("Found the following notes:")
    print("\n".join([str(record) for record in results]))

    # Step 4: Confirm the user wants to delete the note
    confirm = input(f"Are you sure you want to delete the note titled '{results[0].title}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        # Deleting the note
        del note.data[results[0].title]
        return f"Note '{results[0].title}' has been deleted."
    else:
        return "Deletion cancelled."