from room import Room
from hotel import Hotel
from boutiqueHotel import BoutiqueHotel
from resortHotel import ResortHotel
from businessHotel import BusinessHotel

hotel = Hotel()

room1 = Room(101)
room2 = Room(102)
room3 = Room(103)
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)


print("")
print("")
# Повинен вивести повідомлення про бронювання
print(hotel.book_room(101, "John", "2023-09-25", "2023-09-28"))
print("")
print("")
# Повинен вивести повідомлення про вже заброньований номер
print(hotel.book_room(101, "Alice", "2023-10-01", "2023-10-03"))  
print("")
print("")
print(hotel.add_review("Mary", "Great hotel with friendly staff."))

# Обслуговування номеру
print(hotel.room_service(101))  # Повинен вивести повідомлення про прибирання
print("")
print("")
print(hotel.room_service(102))  # Повинен вивести повідомлення про помилку (номер не заброньований)
print("")
print("")


# Отримання списку номерів, заброньованих номерів і відгуків
print("All rooms:")
hotel.get_rooms()
print("")
print("")

print("Booked rooms:")
hotel.get_booked_rooms()
print("")
print("")

print("Reviews:", hotel.get_reviews())




# Створюємо готель типу BusinessHotel
print("")
print("")
business_hotel = BusinessHotel()

# Додаємо номери до готелю
print("")
print("")
room4 = Room(201)
room5 = Room(202)
business_hotel.add_room(room4)
business_hotel.add_room(room5)

# Бронюємо номери у бізнес-готелі
print("")
print("")
print(business_hotel.book_room(201, "Sarah", "2023-10-10", "2023-10-15"))  # Повинен вивести повідомлення про бронювання

# Організовуємо конференцію в бізнес-готелі
print("")
print("")
print(business_hotel.organize_conference())  # Повинен вивести повідомлення про конференцію

# Створюємо готель типу BoutiqueHotel
print("")
print("")
boutique_hotel = BoutiqueHotel()

# Додаємо номери до готелю
print("")
print("")
room6 = Room(301)
room7 = Room(302)
boutique_hotel.add_room(room6)
boutique_hotel.add_room(room7)

# Бронюємо номери в бутик-готелі
print("")
print("")
print(boutique_hotel.book_room(301, "Michael", "2023-11-01", "2023-11-05"))  # Повинен вивести повідомлення про бронювання

# Проводимо обслуговування номеру в бутик-готелі
print("")
print("")
print(boutique_hotel.champagne_in_the_room(301))  # Повинен вивести повідомлення про обслуговування

# Створюємо готель типу ResortHotel
print("")
print("")
resort_hotel = ResortHotel()

# Додаємо номери до готелю
print("")
print("")
room8 = Room(401)
room9 = Room(402)
resort_hotel.add_room(room8)
resort_hotel.add_room(room9)

# Відвідуємо спа-салон у курортному готелі
print("")
print("")
print(resort_hotel.spa())  # Повинен вивести повідомлення про відвідування спа

# Приєднуємося до екскурсії у курортному готелі
print("")
print("")
print(resort_hotel.excursion())  # Повинен вивести повідомлення про екскурсію

# Організовуємо концерт у курортному готелі
print("")
print("")
print(resort_hotel.organize_concert())  # Повинен вивести повідомлення про концерт
