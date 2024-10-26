from elevator import Elevator

class Building:#ex2
    def __init__(self,bottom,top,elevators):
        self.elevators = []
        for i in range (elevators):
            self.elevators.append(Elevator(bottom,top))

    def run_elevator (self, elevator_num, floor):
        print(f"Elevator {elevator_num} is moving")
        self.elevators[elevator_num -1].go_to_floor(floor)

    def fire_alarm(self):# ex 3
        print ("Fire alarm")
        for e in self.elevators:
            e.go_to_floor(e.bottom)

print("\n Elevator is in the Building")
building1 = Building (1,7, 3)
building1.run_elevator(1,4)
building1.run_elevator(2,5)
building1.run_elevator(3,3)
building1.fire_alarm()