from math import sqrt as square_root
import random

class Pi:

    def __init__(self, iterations = 0):
        self.iterations = iterations
        self.total_points = 0
        self.points_inside_circle = 0
        self.x_cood = 0
        self.y_cood = 0

    def generate_random(self):
        return random.uniform(0,1)
    
    def generate_points(self):
        self.x_cood = self.generate_random()
        self.y_cood = self.generate_random()

    def distance(self):
        return square_root(self.x_cood**2 + self.y_cood**2)

    def calculate(self):
        for _ in range(self.iterations):
            self.x_cood = random.uniform(0,1)
            self.y_cood = random.uniform(0,1)
            distance = square_root(self.x_cood**2 + self.y_cood**2)

            if distance < 1:
                self.points_inside_circle += 1
            
            self.total_points += 1
            
        return (4*self.points_inside_circle/self.total_points)




pi = Pi(100)
print(random.uniform(0,1))s



