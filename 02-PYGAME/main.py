import pygame 
import sys
import random

# Intialize pygame 
pygame.init() 

# Creat the screen 
screen = pygame.display.set_mode((800, 600))


# Player variables
playerX = 370
playerY = 480
playerX_change = 0

# Enemy variables
enemyX = random.randint(0, 800)
enemyY = random.randint(20, 100)
enemyX_change = 2
enemyY_change = 0

# Bullet variables
bulletX = 200
bulletY = 200
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

# Importing player image 
playerImg = pygame.image.load('player.png')

# Importing backdrop image 
backgroundImg = pygame.image.load('background.jpeg')

# Importing enemy image
enemyImg = pygame.image.load('enemy.png')

# Importing bullet image
bulletImg = pygame.image.load('bullet.png')

def fire_bullet(x, y):
    screen.blit(bulletImg, (x, y))

while True:
    screen.blit(backgroundImg, (0, 0))
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

    # Enemy boundry bounce off
    if enemyX > 736 or enemyX < 0:
        enemyX_change = - enemyX_change
        enemyY += 20

    playerX = playerX + playerX_change
    enemyX = enemyX + enemyX_change
    fire_bullet(200, 200)

    screen.blit(playerImg, (playerX, playerY))
    screen.blit(enemyImg, (enemyX, enemyY))  
    pygame.display.update()