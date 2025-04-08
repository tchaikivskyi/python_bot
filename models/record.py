from models.name import Name
from models.phone import Phone


class Record:

    def __init__(self, first_name, last_name, email, phones, birthday_date):
        self.first_name = Name(first_name)
        self.last_name = Name(last_name)
        self.email = email
        self.phones = [phones]
        self.birthday = birthday_date

    def __str__(self):
        phones = "; ".join(p for p in self.phones)
        return f"Contact name: {self.first_name} {self.last_name}, email: {self.email},phones: {phones}, birthday: {self.birthday}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # def remove_phone(self, phone):
    #     for p in self.phones:
    #         if p.value == phone:
    #             self.phones.remove(p)
    #             return True
    #     return False

    # def edit_phone(self, old_phone, new_phone):
    #     for p in self.phones:
    #         if p.value == old_phone:
    #             self.phones.remove(p)
    #             self.add_phone(new_phone)
    #             return True
    #     return False

    # def find_phone(self, phone):
    #     for p in self.phones:
    #         if p.value == phone:
    #             return p
    #     return None

    # def add_birthday(self, birthday_date):
    #     self.birthday = Birthday(birthday_date)
