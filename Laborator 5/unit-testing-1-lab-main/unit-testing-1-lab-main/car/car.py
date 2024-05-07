class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.distance = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.distance += self.speed
        self.time += 1

    def average_speed(self):
        return self.distance / self.time
