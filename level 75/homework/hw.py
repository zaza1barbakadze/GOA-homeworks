class Car:
    def __init__(self, brand, model, year, engine_volume):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
    
    def get_description(self):
        return f"{self.brand} {self.model}, {self.year}, {self.engine_volume}L"

car1 = Car("Toyota", "Prius", 2018, 1.8)
print(car1.get_description())