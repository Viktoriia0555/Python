import random
import threading
import time

class Cafe:
    def __init__(self, num_tables, num_waiters):
        self.tables = [{'occupied': False} for _ in range(num_tables)]
        self.waiters = [{'capacity': 3, 'assigned': False} for _ in range(num_waiters)]
        self.clients = []
        self.total_clients_served = 0
        self.lock = threading.Lock()  

    def assign_waiter(self):
        with self.lock:
            for waiter in self.waiters:
                if not waiter['assigned']:
                    waiter['assigned'] = True
                    return waiter

    def simulate(self, opening_time, closing_time):
        current_time = opening_time
        while current_time < closing_time:
            
            if random.random() < 0.6:  # Шанс
                self.clients.append({'wait_time': random.randint(5, 20), 'service_time': random.randint(15, 40)})
            
            
            for client in self.clients:
                if client['wait_time'] > 0:
                    client['wait_time'] -= 1
                else:
                    assigned_waiter = self.assign_waiter()
                    if assigned_waiter:
                        assigned_waiter['capacity'] -= 1
                        if assigned_waiter['capacity'] <= 0:
                            assigned_waiter['assigned'] = False
                        self.total_clients_served += 1
                        client['service_time'] -= 1
                    else:
                        self.clients.remove(client)

            
            current_time += 1

        return self.total_clients_served

class Client:
    def __init__(self, wait_time, service_time):
        self.wait_time = wait_time
        self.service_time = service_time
