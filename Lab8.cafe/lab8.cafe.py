import random
import time

class Cafe:
    def __init__(self, num_tables, num_waiters, peak_hours):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.tables = [{'occupied': False, 'reserved': False} for _ in range(num_tables)]
        self.waiters = [False] * num_waiters
        self.profit = 0
        self.peak_hours = peak_hours
        self.hourly_profits = []
        self.busy_hours = []
        self.idle_hours = []

    def simulate(self, simulation_hours):
        for hour in range(simulation_hours):
            num_customers = self.generate_num_customers(hour)
            
            hourly_profit = 0

            for _ in range(num_customers):
                free_table = self.get_free_table()
                free_waiter = self.get_free_waiter()

                if free_table is not None and free_waiter is not None:
                    time_spent = random.randint(30, 120)
                    wait_time = random.randint(5, 30)
                    hourly_profit += self.serve_customer(free_table, free_waiter, time_spent, wait_time)

            self.free_up_tables_and_waiters()

            print(f"Година {hour + 1}: Кількість клієнтів - {num_customers}, Прибуток: {hourly_profit}")

            # Запис прибутку за годину
            self.hourly_profits.append(hourly_profit)

            # Запис годин, коли найбільше та найменше завантажені
            if hourly_profit == max(self.hourly_profits):
                self.busy_hours.append(hour + 1)
            elif hourly_profit == min(self.hourly_profits):
                self.idle_hours.append(hour + 1)

            # Затримка для реалістичності симуляції
            time.sleep(1)

        print(f"Загальний прибуток: {self.profit}")
        print(f"Найбільш завантажені години: {self.busy_hours}")
        print(f"Найменш завантажені години: {self.idle_hours}")

    def generate_num_customers(self, hour):
        # Генерація кількості клієнтів залежно від години
        if hour in self.peak_hours:
            return random.randint(5, 15)  # більше клієнтів у пікові години
        else:
            return random.randint(1, 5)

    def get_free_table(self):
        for i, table in enumerate(self.tables):
            if not table['occupied'] and not table['reserved']:
                self.tables[i]['occupied'] = True
                return i
        return None

    def reserve_table(self, table_number):
        if not self.tables[table_number]['occupied']:
            self.tables[table_number]['reserved'] = True
            print(f"Столик {table_number + 1} заброньований.")

    def get_free_waiter(self):
        for i, occupied in enumerate(self.waiters):
            if not occupied:
                self.waiters[i] = True
                return i
        return None

    def serve_customer(self, table, waiter, time_spent, wait_time):
        # Логіка обслуговування клієнта
        print(f"Клієнт сідає за столик {table + 1} і чекає офіціанта {waiter + 1}.")
        
        # Очікування офіціанта
        time.sleep(wait_time)
        
        # Обслуговування клієнта
        profit = random.randint(10, 50)
        print(f"Столик {table + 1} обслуговується офіціантом {waiter + 1}. Прибуток: {profit}")
        self.profit += profit
       
        return profit

    def free_up_tables_and_waiters(self):
        # Звільнення столиків та офіціантів після завершення обслуговування
        for i, table in enumerate(self.tables):
            if table['occupied'] and not table['reserved']:
                self.tables[i]['occupied'] = False
        self.waiters = [False] if all(self.waiters) else self.waiters

    def optimize_service(self):
        # Аналіз симуляції та стратегії поліпшення обслуговування
        max_profit_index = self.hourly_profits.index(max(self.hourly_profits))
        min_profit_index = self.hourly_profits.index(min(self.hourly_profits))

        print(f"Найбільш завантажені години: Година {max_profit_index + 1}")
        print(f"Найменш завантажені години: Година {min_profit_index + 1}")

        # Перевірка часу, коли кафе має найменший прибуток
        if min_profit_index > max_profit_index:
            print("Стратегія: Запропонувати знижку або спеціальні акції у 'мертві' години для збільшення відвідуваності.")

    def set_num_tables(self, num_tables):
        # Змінити кількість столиків
        self.num_tables = num_tables
        self.tables = [{'occupied': False, 'reserved': False} for _ in range(num_tables)]

    def set_num_waiters(self, num_waiters):
        # Змінити кількість
        self.num_waiters = num_waiters
        self.waiters = [False] * num_waiters

    def set_peak_hours(self, peak_hours):
        # Змінити години пікового навантаження
        self.peak_hours = peak_hours

# Параметри кафе
num_tables = 10
num_waiters = 3
peak_hours = [12, 13, 18, 19]  # Пікові години: обід і вечеря

# Створення об'єкту кафе та симуляція протягом 12 годин
cafe = Cafe(num_tables, num_waiters, peak_hours)

# Зміна параметрів кафе
cafe.set_num_tables(15)
cafe.set_num_waiters(5)
cafe.set_peak_hours([13, 14, 19, 20])

# Симуляція з бронюванням столиків
cafe.reserve_table(2)
cafe.reserve_table(5)

# Симуляція протягом 12 годин
cafe.simulate(12)

# Аналіз та стратегії поліпшення обслуговування
cafe.optimize_service()
