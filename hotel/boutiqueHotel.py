from hotel import Hotel


class BoutiqueHotel(Hotel):
    def champagne_in_the_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.room_status == "Free":
                    return "This room isn't booked"
                else:
                    return f"The waiter brought champagne to the room №{room_number}"
        return f"Room {room_number} is not found."
    

