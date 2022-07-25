import sys
 
import pygame
from pygame.locals import *
from breaker import Breaker
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Creating objects
breaker = Breaker(width/2, height/2) 
 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  breaker.move(3)
  breaker.ifOnEdgeBounce()

  # Draw.
  breaker.draw(screen)

  pygame.display.flip()
  fpsClock.tick(fps)