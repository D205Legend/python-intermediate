import math 

class Player:
    color = (255, 0, 0)

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.x_vel = 0
        self.y_vel = 0

    def touching(self, food):
        sq_of_dist = (self.x - food.x) ** 2 + (self.y - food.y) ** 2 
        distance = math.sqrt(sq_of_dist)

        if distance < (self.radius + food.size):
            return True
        else:
            return False