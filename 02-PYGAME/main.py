import pygame 
import sys

# Intialize pygame 
pygame.init() 

# Creat the screen 
screen = pygame.display.set_mode((800, 600))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()