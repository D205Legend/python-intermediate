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
        #self.x_vel = speed
        #self.y_vel = speed
        self.x += self.x_vel * speed
        self.y += self.y_vel * speed

    def ifOnEdgeBounce(self, screen):
        width, height = screen.get_size()
        # If touching right edge or left edge
        if self.x + self.size > width or self.x < 0:
            self.x_vel *= -1

        if self.y < 0 or self.y + self.size > height:
            self.y_vel *= -1
