from collections import UserDict
from datetime import datetime, timedelta
from models.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = f"{record.first_name.value} {record.last_name.value}"
        self.data[key] = record

    def find_by_full_name(self, full_name: str):
        return self.data.get(full_name.lower().strip())

    def find_by_query_field(self, query: str):
        query = query.lower().strip()
        results = []

        for key, record in self.data.items():
            if (
                query in key.lower()
                or query in record.first_name.value.lower()
                or query in record.last_name.value.lower()
                or query in record.email.value.lower()
                or any(query in phone.value.lower() for phone in record.phones)
                or (hasattr(record, "address") and query in record.address.lower())
            ):
                results.append(record)
                continue  # шукаємо далі

        if record.birthday:
            bday_str = record.birthday.value.strftime("%d.%m.%Y")
            bday_day = record.birthday.value.strftime("%d")
            bday_month = record.birthday.value.strftime("%m")
            bday_year = record.birthday.value.strftime("%Y")

            if (
                query in bday_str
                or query == bday_day
                or query == bday_month
                or query == bday_year
            ):
                results.append(record)

        return results if results else None

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
