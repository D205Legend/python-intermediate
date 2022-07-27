import sys
 
import pygame
from pygame.locals import *
from breaker import Breaker
from player import Player
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Creating objects
breaker = Breaker(width/2, height/2) 
player = Player(width/2, height * 0.9)

# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  mouseX, mouseY = pygame.mouse.get_pos()
  player.x = mouseX
  breaker.move(2)
  breaker.ifOnEdgeBounce(screen)

  # Draw.
  breaker.draw(screen)
  player.draw(screen)

  pygame.display.flip()
  fpsClock.tick(fps)