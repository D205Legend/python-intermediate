import sys
import random
from food import *
from player import *

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 960, 540
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
mouse_x = 0
mouse_y = 0
NUM_FOOD = 150
FOOD_SIZE = 15
foods = []

# Creating food items
for i in range(NUM_FOOD):
    food_x = random.randint(FOOD_SIZE, width - FOOD_SIZE)
    food_y = random.randint(FOOD_SIZE, height - FOOD_SIZE)
    food = Food(food_x, food_y)
    foods.append(food)


# Creating player object
player = Player(width/2, height/2)

# Creating the Background
backdrop = pygame.image.load('background.jpg')

# Sounds 
chomp = pygame.mixer.Sound('Suction Cup.wav')

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    player.x += player.x_vel
    player.y += player.y_vel
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.x_vel = (mouse_x - player.x) * 0.1
    player.y_vel = (mouse_y - player.y) * 0.1
    
    # Edge sensing
    if player.x < player.radius:
        player.x = player.radius
    if player.x > (width - player.radius):
        player.x = width - player.radius
    if player.y < player.radius:
        player.y = player.radius
    if player.y > (height - player.radius):
        player.y = height - player.radius

    # Touch sensing food
    for food in foods:
        if player.touching(food):
            pygame.mixer.Sound.play(chomp)
            player.radius += 1
            foods.remove(food)

    # Draw.
    screen.blit(backdrop, (0, 0))
    for food in foods:
        pygame.draw.circle(screen, food.color, (food.x, food.y), food.size)
    pygame.draw.circle(screen, RED, (player.x, player.y), player.radius)
    pygame.display.flip()
    fpsClock.tick(fps)