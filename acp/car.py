class Ferrari:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} Ferrari's engine roars to life!"

    def accelerate(self):
        return f"The {self.model} Ferrari accelerates with incredible speed."

    def stop_engine(self):
        return f"The {self.model} Ferrari's engine is turned off."

class Bmw:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The {self.model} BMW's engine smoothly starts."

    def accelerate(self):
        return f"The {self.model} BMW accelerates with refined power."

    def stop_engine(self):
        return f"The {self.model} BMW's engine is quietly shut down."

def perform_car_actions(car):
    """
    This function demonstrates polymorphism by calling common methods
    on different car objects without knowing their specific types.
    """
    print(car.start_engine())
    print(car.accelerate())
    print(car.stop_engine())
    print("-" * 30)


ferrari_488 = Ferrari("488 GTB")
bmw_m3 = Bmw("M3")


perform_car_actions(ferrari_488)
perform_car_actions(bmw_m3)