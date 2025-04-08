class RecordNote:
    def __init__(self, title, description = "", tags = []):
        self.title = title
        self.description = description
        self.tags = tags

    def __str__(self):
        return f"Note title: {self.title}"



 
