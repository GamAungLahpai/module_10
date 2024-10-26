from module9 import Car
import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(self.name + ":")
        print("Reg_Plate Speed Travel_distance")
        print("---------------------------------")
        for car in self.cars:
            print(f"{car.registration_number:6s}: {car.current_speed:3d}km/h, {car.travelled_distance} ")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            return False

cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

race = Race ("Grand Demolition Derby", 8000, cars)
x = 0
while not race.race_finished():
    race.hour_passes()
    x += 1
    if x%10 == 0:
        print(f"After {x} hours")
        race.print_status()

print(f"Final result after {x} hours")
race.print_status()
