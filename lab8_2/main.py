from cafe import Cafe
import threading

def simulate_cafe_day(cafe, opening_time, closing_time):
    cafe.simulate(opening_time, closing_time)

if __name__ == "__main__":
    num_tables = 10
    num_waiters = 3
    opening_time = 10
    closing_time = 22

    cafe = Cafe(num_tables, num_waiters)
    threads = []
    num_simulations = 5  # Кількість одночасних симуляцій

    for _ in range(num_simulations):
        thread = threading.Thread(target=simulate_cafe_day, args=(cafe, opening_time, closing_time))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Загальна кількість обслужених клієнтів: {cafe.total_clients_served}")
