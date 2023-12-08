from random import randint

class Cafe:
    def init(self, tables, waiters):
        self.tables = tables
        self.waiters = waiters
        self.clientlist = []

class Clients:
    def init(self, sizeOfCompany, time):
        self.sizeOfCompany = sizeOfCompany
        self.time = time

tables_count = randint(5, 15)
waiters_count = randint(2, 5) * 2
cafe = Cafe(tables_count, waiters_count)

more_tables_count = 0
more_waiters_count = 0
max_clients_time = 0
min_clients_time = float('inf')

print(f"Інформація про кафе: Столи - {tables_count}, Офіціанти - {waiters_count // 2}")

for hour in range(1, 13):
    num_clients = randint(1, 10)

    if num_clients > max_clients_time:
        max_clients_time = num_clients
    if num_clients < min_clients_time:
        min_clients_time = num_clients

    if num_clients > cafe.tables:
        more_tables_count += 1
        more_tables = num_clients - cafe.tables
        cafe.tables += more_tables
    
    if num_clients > cafe.waiters // 2:
        more_waiters_count += 1
        more_waiters = (num_clients - (cafe.waiters // 2)) * 2
        cafe.waiters += more_waiters

print(f"Закінчився день. Залишилося столів: {cafe.tables}, Залишилося офіціантів: {cafe.waiters // 2}")
print(f"Ситуації, коли не вистачало столів: {more_tables_count}")
print(f"Ситуації, коли не вистачало офіціантів: {more_waiters_count}")
print(f"Час із максимальною кількістю клієнтів: {max_clients_time}")
print(f"Час із мінімальною кількістю клієнтів: {min_clients_time}")

if more_tables_count > 3:
    print("Рекомендується збільшити кількість столів.")
elif more_tables_count == 0:
    print("Кількість столів достатня.")

if more_waiters_count > 3:
    print("Рекомендується збільшити кількість офіціантів.")
elif more_waiters_count == 0:
    print("Кількість офіціантів достатня.")