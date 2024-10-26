class Elevator:
    def __init__(self,bottom,top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Elevator is moving from {self.current} to {self.current+1}")
            self.current += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range (floor - self.current):
                if not self.floor_up():
                    break

        elif floor < self.current:
            for i in range (self.current - floor ):
                if not self.floor_down():
                    break
        else:
            print(f"Elevator is already at the required floor{self.current}")












