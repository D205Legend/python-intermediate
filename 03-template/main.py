import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
circle_X, circle_Y = 300, 200
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# Game loop.
while True:
  screen.fill((255, 255, 255))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            circle_X += 5
  
  # Update.
  
  # Draw.
  pygame.draw.circle(screen, "RED", (circle_X, circle_Y), 50, 0)
  
  pygame.display.flip()
  fpsClock.tick(fps)