from collections import UserDict
from models.record_note import RecordNote



class NotesBook(UserDict):
    def add_record(self, record: RecordNote):
        self.data[record.title] = record

    def find(self, title):
        return self.data.get(title)

    def delete(self, title):
        return self.data.pop(title)

    def search_by_tag(self, tag):
        matching_notes = [
            record for record in self.data.values() if tag in record.tags
        ]
        return matching_notes
