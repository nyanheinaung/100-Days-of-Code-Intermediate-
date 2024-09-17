from car import Car
import random

MAX_TOTAL_CARS = 20


class GameManager:
    def __init__(self):
        self.sleep_time = 1
        self.cars = []

    def faster(self):
        self.sleep_time = max(0.01, self.sleep_time * 0.9)

    def initial_cars(self):
        for i in range(MAX_TOTAL_CARS//3):
            self.spawn_car("inside")
        for i in range(2*MAX_TOTAL_CARS//3):
            self.spawn_car("outside")

    def choose_direction(self):
        if random.randint(0,1):
            return 1
        else:
            return -1

    def inside_position(self):
        initial_x = random.randint(-300, 300)
        initial_y = random.randint(-250, 250)
        position = (initial_x, initial_y)
        return position

    def outside_position(self, direction):
        if direction == 1:
            initial_x = random.randint(-600, -300)
        else:
            initial_x = random.randint(300, 600)

        initial_y = random.randint(-250, 250)
        position = (initial_x, initial_y)
        return position

    def spawn_car(self, side):
        direction = self.choose_direction()
        if side == "inside":
            position = self.inside_position()
        else:
            position = self.outside_position(direction)

        new_car = Car(direction, position)
        self.cars.append(new_car)

    def next_stage(self):
        self.faster()
        self.initial_cars()


    def check_collision(self, player):
        for car in self.cars:
            car.move()
            if car.xcor() < -600 or car.xcor() > 600:
                car.going = False
                car.remove_car()
                self.spawn_car("outside")
            if -50 < car.xcor() - player.xcor() < 50 and -10 < car.ycor() - player.ycor() < 10:
                return True
        return False
