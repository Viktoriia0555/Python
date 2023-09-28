from datetime import date
from room import Room


class Hotel:
    def __init__(self):
        self.rooms = []
        self.booked_rooms = []
        self.reviews = []

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)
        else:
            raise TypeError("The argument must be a Room class instance")

    def book_room(self, room_number, guest_name, check_in_date, check_out_date):
        for room in self.rooms:
            if room.number == room_number:
                if room.room_status == "Free":
                    room.room_status = "Booked"
                    room.room_service_date = f"{check_in_date} to {check_out_date}"
                    self.booked_rooms.append(room)
                    return f"{guest_name} has booked room {room_number} from {check_in_date} to {check_out_date}."
                else:
                    return f"Room {room_number} is already booked for {room.room_service_date}."
        return f"Room {room_number} is not found."

    def add_review(self, user_name, review_text):
        self.reviews.append({"User": user_name, "Review": review_text})
        return f"{user_name} has left a review about the hotel: {review_text}"

    def room_service(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.room_status == "Free":
                    return "This room isn't booked"
                else:
                    room.room_service_date = date.today()
                    return f"Room {room.number} was cleaned"
        return f"Room {room_number} is not found."

    def get_rooms(self):
        for room in self.rooms:
            print(room)

    def get_booked_rooms(self):
        for room in self.booked_rooms:
            print(room)

    def get_reviews(self):
        return self.reviews

