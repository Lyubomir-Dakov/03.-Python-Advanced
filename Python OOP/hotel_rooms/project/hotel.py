from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        free_rooms_numbers = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms_numbers = ', '.join(str(room.number) for room in self.rooms if room.is_taken)
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {free_rooms_numbers}\n"
        result += f"Taken rooms: {taken_rooms_numbers}"
        return result
