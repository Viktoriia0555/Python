import random


class Hotel:
  def __init__(self, hotel_name, available_services=set()):
    self.hotel_name = hotel_name
    self.available_services = available_services
  
class Service(Hotel):
  def __init__(self, service_name, services_offered):
    super().__init__(service_name, services_offered)
    self.service_name = service_name
  
  def serve(self, customer):
    while any(customer.needs.values()):
      for need, need_value in customer.needs.items():
        if need in self.available_services and self.available_services[need] > 0:
          if self.available_services[need] >= need_value:
            customer.needs[need] = 0
          else:
            customer.needs[need] -= self.available_services[need]
      customer.needs = {k: round(v, 2) for k, v in customer.needs.items()}
      print(vars(customer))

class BarService(Service):
  def __init__(self, service_name, services_offered):
    super().__init__(service_name, services_offered)
  
class Customer:
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.needs = self.generate_random_needs()

  def generate_random_needs(self):
    random_needs = {'eat', 'bar', 'child room', 'massage'}
    random_values = {need: round(random.uniform(0.1, 1.0), 1) for need in random.sample(random_needs, 2)}
    
    return random_values

customer = Customer("John")
hotel = Hotel("Business Hotel", available_services={"eat": 0.5, "bar": 0.35, "child room": 0.25, 'massage': 0.5})
hotel_service = Service(hotel.hotel_name, hotel.available_services)
hotel_service.serve(customer)
