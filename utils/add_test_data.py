from datetime import datetime
from models.record import Record
from models.record_note import RecordNote
from utils.colored_text import colored_text

def add_test_data(book, note):
    contacts = [
        {
            "first_name": "Alice",
            "last_name": "Note",
            "email": "alice.note@example.com",
            "phones": ["1234567891"],
            "birthday_date": datetime(1990, 5, 15).date(),
            "address": "101 Main Street, New York, NY"
        },
        {
            "first_name": "Alicia",
            "last_name": "Noteson",
            "email": "alicia.noteson@example.com",
            "phones": ["1234567892"],
            "birthday_date": datetime(1985, 8, 22).date(),
            "address": "202 Central Avenue, Los Angeles, CA"
        },
        {
            "first_name": "Mark",
            "last_name": "Peterson",
            "email": "mark.peterson@example.com",
            "phones": ["1234567893"],
            "birthday_date": datetime(1992, 11, 3).date(),
            "address": "303 Elm Street, Chicago, IL"
        },
        {
            "first_name": "Linda",
            "last_name": "Green",
            "email": "linda.green@example.com",
            "phones": ["1234567894"],
            "birthday_date": datetime(1988, 3, 12).date(),
            "address": "404 Oak Lane, Houston, TX"
        },
        {
            "first_name": "Tom",
            "last_name": "Henderson",
            "email": "tom.henderson@example.com",
            "phones": ["1234567895"],
            "birthday_date": datetime(1995, 7, 28).date(),
            "address": "505 Pine Road, Miami, FL"
        }
    ]

    for contact in contacts:
        record = Record(**contact)
        book.add_record(record)

    notes = {
        "Note Reminder": RecordNote(
            title="Note Reminder",
            description="This is a simple reminder about a note you created.",
            tags=["reminder", "note"]
        ),
        "Notes Overview": RecordNote(
            title="Notes Overview",
            description="A quick summary of all important notes and ideas.",
            tags=["summary", "note"]
        ),
        "Vacation Plans": RecordNote(
            title="Vacation Plans",
            description="List of places to visit and things to pack for the trip.",
            tags=["travel", "fun"]
        ),
        "Meeting Summary": RecordNote(
            title="Meeting Summary",
            description="Key points discussed during the weekly team meeting.",
            tags=["work", "summary"]
        ),
        "Book Wishlist": RecordNote(
            title="Book Wishlist",
            description="Books to read this year including fiction and non-fiction.",
            tags=["books", "wishlist"]
        )
    }

    note.update(notes)

    colored_text("Added 5 test contacts and 5 test notes with partial similarity for search testing.", "green")
