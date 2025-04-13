from decorators.error_handlers import input_error
from models.notes_book import NotesBook
from models.record_note import RecordNote
from rich.console import Console
from utils.table import dynamic_table
from utils.parse_to_dict import parse_data_str_to_dict
from utils.colored_text import colored_input, colored_text
from utils.parse_to_dict import parse_data_str_to_dict_notes
from utils.input_validate import input_validate_field

console = Console()

@input_error
def add_note(note: NotesBook):
    title = input_validate_field("Enter title", length=2, field_type="title")
    description = colored_input("Enter text", "blue")
    tags = colored_input("Enter tags separated by commas", "blue")
    tags = [tag.strip() for tag in tags.split(",")] if tags else []

    new_note = {
        "title": title,
        "description": description,
        "tags": tags
    }

    record = RecordNote(**new_note)
    note.add_record(record)

    return colored_text("Note is saved")


@input_error
def show_all(_, note: NotesBook):
    if not note.data:
        return "Your notes book is empty!"
    
    rows = [parse_data_str_to_dict_notes(str(record)) for record in note.data.values()]
    dynamic_table(title="All notes", rows=rows, style="cyan")
    

@input_error
def search_by_tag(_, note: NotesBook):
    tag_to_search = colored_input("Enter the tag to search for", "blue").strip()

    if not tag_to_search:
        return colored_text("Tag cannot be empty")

    matching_notes = [
        record for record in note.data.values() if tag_to_search in record.tags
    ]

    if not matching_notes:
        return colored_text(f"No notes found with the tag '{tag_to_search}'", "yellow")
  
    rows = [parse_data_str_to_dict_notes(str(record)) for record in matching_notes]
    dynamic_table(title="Notes found", rows=rows, style="cyan")


@input_error
def sort_by_tags(_, note: NotesBook):
    if not note.data:
        return colored_text("Your notes book is empty!")

    sorted_notes = sorted(note.data.values(), key=lambda record: record.tags[0] if record.tags else "")

    rows = [parse_data_str_to_dict_notes(str(record)) for record in sorted_notes]
    dynamic_table(title="Notes sorted", rows=rows, style="cyan")

# Function search notes by title
@input_error
def search_note_by_title(note: NotesBook):
    while True:
        query = colored_input("Enter Note's Title", "blue").strip().lower()
        
        if query:
            break
        else:
            colored_text("Title cannot be empty. Please enter a valid title.", "red")
    
    results = [record for record in note.data.values() if query in record.title.lower()]

    if not results:
        return colored_text(f"No notes found with title '{query}'.", "yellow")

    data_string = [parse_data_str_to_dict_notes(str(record)) for record in results]
    
    dynamic_table(
        title="Search result",
        rows=data_string,
        style="cyan"
    )



# Function edit note
@input_error
def edit_note(note: NotesBook):
    title_to_edit = colored_input("Enter note's title to edit", "blue").strip().lower()

    results = [
        record for record in note.data.values()
        if title_to_edit == record.title.lower()
    ]

    if not results:
        colored_text(f"No notes found with title '{title_to_edit}'.", "yellow")
        return

    note_to_edit = results[0]
    original_title = note_to_edit.title

    colored_text("\nEdit options ")
    colored_text("1 - Edit Title", "cyan")
    colored_text("2 - Edit Description", "cyan")
    colored_text("3 - Edit Tags\n", "cyan")

    choice = colored_input("Choose what to edit (1-3):", "blue").strip()

    match choice:
        case "1":  # Edit Title
            new_title = colored_input("Enter a new title", "cyan").strip()
            if new_title and new_title != original_title:
                note_to_edit.title = new_title
                note.data[new_title] = note_to_edit
                del note.data[original_title]
                colored_text("Title updated successfully.")
            else:
                colored_text("No changes made or same title entered.", "yellow")

        case "2":  # Edit Description
            new_desc = colored_input("Enter a new description", "cyan").strip()
            if new_desc and new_desc != note_to_edit.description:
                note_to_edit.description = new_desc
                colored_text("Description updated successfully.")
            else:
                colored_text("No changes made or same description entered.", "yellow")

        case "3":  # Edit Tags
            current_tags = ', '.join(note_to_edit.tags)
            colored_text(f"Current tags: {current_tags}", "cyan")
            colored_text("\nEdit tag options")
            colored_text("1 - Add new tag", "cyan")
            colored_text("2 - Edit tag", "cyan")
            colored_text("3 - Delete tag\n", "cyan")

            tag_action = colored_input("Choose action: (1-3)", "blue").strip()

            match tag_action:
                case "1":
                    new_tag = colored_input("Enter new tag to add", "cyan").strip()
                    if new_tag and new_tag not in note_to_edit.tags:
                        note_to_edit.tags.append(new_tag)
                        colored_text("Tag added.")
                    else:
                        colored_text("Tag already exists or empty.", "yellow")

                case "2":
                    old_tag = colored_input("Enter the tag to replace", "cyan").strip()
                    if old_tag in note_to_edit.tags:
                        new_tag = colored_input("Enter the new tag", "cyan").strip()
                        idx = note_to_edit.tags.index(old_tag)
                        note_to_edit.tags[idx] = new_tag
                        colored_text("Tag updated.")
                    else:
                        colored_text("Old tag not found.", "yellow")

                case "3":
                    tag_to_remove = colored_input("Enter the tag to delete", "cyan").strip()
                    if tag_to_remove in note_to_edit.tags:
                        note_to_edit.tags.remove(tag_to_remove)
                        colored_text("Tag deleted.")
                    else:
                        colored_text("Tag not found.", "yellow")

                case _:
                    colored_text("Invalid tag action.", "red")
        case _:
            colored_text("Invalid option!", "red")

    
# Function delete note
@input_error
def delete_note(note: NotesBook):
    # Step 1: Ask for the note's title to be deleted and ensure it's not empty
    while True:
        title_to_delete = colored_input("Enter Note's Title to be deleted", "blue").strip().lower()

        if title_to_delete:
            break
        else:
            return colored_text("Title cannot be empty. Please enter a valid title.")

    # Step 2: Search for the note by title
    results = [record for record in note.data.values() if title_to_delete in record.title.lower() == title_to_delete]

    if not results:
        return colored_text(f"No notes found with title containing '{title_to_delete}'", "yellow")

    # Step 3: Show the found notes
    colored_text("Found the following notes:")
    # colored_text("\n".join([str(record) for record in results]))
    rows = [parse_data_str_to_dict_notes(str(record)) for record in results]
    dynamic_table(title=f"Note to delete", rows=rows, style="cyan")

    # Step 4: Confirm the user wants to delete the note
    confirm = colored_input(f"Are you sure you want to delete the note titled '{results[0].title}'? (yes/no) ", "blue").strip().lower()

    if confirm == 'yes' or confirm == 'y':
        # Deleting the note
        del note.data[results[0].title]
        return colored_text(f"Note '{results[0].title}' has been deleted")
    else:
        return colored_text("Deletion cancelled")