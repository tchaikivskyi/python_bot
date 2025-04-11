import random
from datetime import datetime
from models.record import Record
from models.record_note import RecordNote
from utils.colored_text import colored_text

def add_test_data(book, note):
    for i in range(1, 6):
        first_name = f"Test"
        last_name = f"User{i}"
        email = f"user{i}@example.com"
        phone = f"123456789{i}"
        
        birthday_datetime = datetime.strptime(
            f"199{i}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}", "%Y-%m-%d"
        )
        birthday = birthday_datetime.date()  

        address = f"123 Test Street Apt {i}"

        contact_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phones": [phone],
            "birthday_date": birthday,  
            "address": address,
        }

        record = Record(**contact_data)
        book.add_record(record)

    for i in range(1, 6):
        note_title = f"Test Note {i}"
        note_obj = RecordNote(
            title=note_title,
            description=f"This is the content of test note {i}.",
            tags=[f"tag{i}", "test"]
        )
        note[note_title] = note_obj

    colored_text("✅ Added 5 test contacts and 5 test notes.", "green")
