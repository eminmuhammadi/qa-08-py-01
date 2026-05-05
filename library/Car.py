class Car:
    def __init__(self, brand, model, year, color, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = fuel_level
        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True

    def stop_engine(self):
        if self.is_engine_on:
            self.is_engine_on = False

    def drive(self, distance):
        fuel_used = distance * 0.1
        self.fuel_level -= fuel_used

    def refuel(self, amount):
        self.fuel_level += amount
