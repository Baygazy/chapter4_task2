class Airplane():

    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        message_take = f"{self.make} {self.model} was take off."
        return message_take

    def fly(self, km):
        self.odometer += km
        message_fly = f"{self.make} flew {self.odometer}km at a speed of {self.max_speed}km/h."
        return message_fly

    def land(self):
        self.is_flying = False
        message_land = f"{self.make} has landed, it's odometer shows {self.odometer}km."
        return message_land

go = Airplane("Boeing", "747", "2019", 600)
print(go.take_off())
print(go.fly(500))
print(go.fly(500))
print(go.land())
# print(go.odometer)
