class Song:
    def __init__(self, name, length, singe):
        self.name = name
        self.length = length
        self.singe = singe

    def get_info(self):
        return f"{self.name} - {self.length}"
