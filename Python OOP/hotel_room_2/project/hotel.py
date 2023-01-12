from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.__find_room_by_number(room_number, self.rooms)
        if not room.is_taken and room.capacity >= people:
            self.guests += people
        room.take_room(people)

    def free_room(self, room_number):
        room = self.__find_room_by_number(room_number, self.rooms)
        self.guests -= room.guests
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {self.__numbers_of_free_rooms(self.rooms)}\n"
        result += f"Taken rooms: {self.__numbers_of_taken_rooms(self.rooms)}"
        return result

    def __numbers_of_free_rooms(self, hotel_rooms):
        result = []
        for room in hotel_rooms:
            if not room.is_taken:
                result.append(room.number)
        return ', '.join([str(x) for x in result])

    def __numbers_of_taken_rooms(self, hotel_rooms):
        result = []
        for room in hotel_rooms:
            if room.is_taken:
                result.append(room.number)
        return ', '.join([str(x) for x in result])

    def __find_room_by_number(self, room_number, hotel_rooms):
        for room in hotel_rooms:
            if room.number == room_number:
                return room
