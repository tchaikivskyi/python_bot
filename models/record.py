from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phones: str,
        birthday_date: str,
    ):
        self.first_name = Name(first_name.lower().strip())
        self.last_name = Name(last_name.lower().strip())
        self.email = Name(email)

        if isinstance(phones, list):
            self.phones = [Phone(p) if not isinstance(p, Phone) else p for p in phones]
        else:
            self.phones = [Phone(phones)]

        self.birthday = Birthday(birthday_date)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"
        return (
            f"Contact name: {self.first_name.value.title()} {self.last_name.value.title()}, "
            f"email: {self.email.value}, phones: {phones}, birthday: {birthday}"
        )

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def change_name(self, new_first, new_last):
        self.first_name = Name(new_first)
        self.last_name = Name(new_last)

    def change_email(self, new_email):
        self.email = Name(new_email)

    def change_address(self, new_address):
        self.address = new_address

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.add_phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)
