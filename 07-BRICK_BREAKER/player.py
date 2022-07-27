import pygame


class Player:
    height = 20
    width = 100
    color = (0, 255, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)