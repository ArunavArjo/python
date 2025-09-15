class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def calculate_fare(self):
        
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def calculate_fare(self):
        
        base_fare = super().calculate_fare()
      
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare


school_bus = Bus("School Volvo", 50)


print(f"Total fare for {school_bus.name} (capacity: {school_bus.capacity}) is: {school_bus.calculate_fare()}")