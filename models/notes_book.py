from collections import UserDict
from models.record_note import RecordNote



class NotesBook(UserDict):
    def add_record(self, record: RecordNote):
        self.data[record.title] = record

    def find(self, title):
        return self.data.get(title)

    def delete(self, title):
        return self.data.pop(title)
