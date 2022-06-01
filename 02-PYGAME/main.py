import pygame 
import sys

# Intialize pygame 
pygame.init() 

# Creat the screen 
screen = pygame.display.set_mode((800, 600))


# Player variables
playerX = 370
playerY = 480
playerX_change = 0

# Importing player image 
playerImg = pygame.image.load('player.png')

# Importing backdrop image 
backgroundImg = pygame.image.load('background.jpeg')


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_LEFT:
                playerX_change = -4
        if event.type == pygame.KEYUP:
            playerX_change = 0        

    # Boundary Detection
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0


    playerX = playerX + playerX_change
    screen.blit(backgroundImg, (0, 0))
    screen.blit(playerImg, (playerX, playerY))  
    pygame.display.update()