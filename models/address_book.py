from collections import UserDict
from datetime import datetime, timedelta
from models.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = f"{record.first_name.value} {record.last_name.value}"
        self.data[key] = record

    def find_by_full_name(self, full_name: str):
        return self.data.get(full_name.lower().strip())

    def delete(self, full_name):
        return self.data.pop(full_name.lower().strip())

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.now().date()
        end_date = today + timedelta(days=days)

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= end_date:
                    upcoming_birthdays.append(record)

        return upcoming_birthdays
