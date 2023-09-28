class Room:
    def __init__(self, number, room_service_date=None, room_status="Free"):
        self.number = number
        self.room_service_date = room_service_date
        self.room_status = room_status

    def __str__(self):
        return f"Room №{self.number},\nStatus: {self.room_status},\nLast time cleaned: {self.room_service_date} \n"