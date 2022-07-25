import pygame


class Breaker:
    size = 10
    color = (255, 0, 0)
    x_vel = 3
    y_vel = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect = pygame.Rect(self.x , self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def move(self, speed):
        self.x_vel = speed
        self.y_vel = speed
        self.x += self.x_vel
        self.y += self.y_vel

    def ifOnEdgeBounce(self, screen):
        pass
