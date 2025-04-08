import pickle
from models.address_book import AddressBook
from models.notes_book import NotesBook

FILENAME_CONTACT = "storage/addressbook.pkl"
FILENAME_NOTE = "storage/notesbook.pkl"


def save_data(data):
    with open(FILENAME_CONTACT, "wb") as f:
        pickle.dump(data["book"], f)
    with open(FILENAME_NOTE, "wb") as f:
        pickle.dump(data["note"], f)


def load_data():
    try:
        with open(FILENAME_CONTACT, "rb") as f:
            book = pickle.load(f)
    except FileNotFoundError:
        book = AddressBook()

    try:
        with open(FILENAME_NOTE, "rb") as f:
            note = pickle.load(f)
    except FileNotFoundError:
        note = NotesBook()

    return {"book": book, "note": note}
