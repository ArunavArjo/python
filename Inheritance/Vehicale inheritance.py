class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

School_Bus = bus("Tung",120,80)
print("Vehicle name:",School_Bus.name,"speed:",School_Bus.max_speed,"mileage",School_Bus.mileage)
