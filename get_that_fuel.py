import pygame
import random
import math

# Intialize pygame modules
pygame.init()

# create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Caption and icon
pygame.display.set_caption("Get That Fuel")
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

# Load background image and set its coordinates
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (width, height))
backgroundX = 0
backgroundY = 0

# Load player image and set its coordinates
player = pygame.image.load('car.png')
playerLeft = player
playerRight = pygame.transform.flip(player, True, False)
playerX = 400
playerY = 460

# Initilaize player speed on the x-axis
playerXSpeed = 0

# Load fuel cans and set their coordinates and speeds randomly
fuelCan = pygame.image.load('gasoline.png')
spawnValue = 4
fuelCanX = []
fuelCanY = []
fuelCanYSpeed = []

for i in range(spawnValue):
    fuelCanX.append(random.randint(0, 800-64))
    fuelCanY.append(random.randint(0, 100))
    fuelCanYSpeed.append(random.randint(2, 5))

# Calculate distance using the distance formula
def distance(playerX, playerY, fuelCanX, fuelCanY):
    distance = math.sqrt(math.pow(playerX - fuelCanX, 2) + (math.pow(playerY - fuelCanY, 2)))
    threshold = 64
    if distance < threshold:
        return True
    else:
        return False

# Player score
score = 0

# Load font
font = pygame.font.Font('freesansbold.ttf', 32)

# Game loop
running = True
while running:
    eventQueue = pygame.event.get()
    for event in eventQueue:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Check if the right arrow key is pressed
            if event.key == pygame.K_RIGHT:
                playerXSpeed = 5
                player = playerRight
            # Check if the left arrow key is pressed
            if event.key == pygame.K_LEFT:
                playerXSpeed = -5
                player = playerLeft

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXSpeed = 0


    # Update x coordinate of the player
    playerX += playerXSpeed

    # Draw background on screen
    screen.blit(background, (backgroundX, backgroundY))
    # Draw player on screen
    screen.blit(player, (playerX, playerY))

    for i in range(spawnValue):
        # Make the fuel cans fall down
        fuelCanY[i] += fuelCanYSpeed[i]
        if fuelCanY[i] > 600:
            fuelCanY[i] = random.randint(0, 100)
        screen.blit(fuelCan, (fuelCanX[i], fuelCanY[i]))

        # Check if a fuel can was grabbed by the player
        caught = distance(playerX, playerY, fuelCanX[i], fuelCanY[i])
        if caught:
            fuelCanX[i] = random.randint(0, 800-64)
            fuelCanY[i] = random.randint(0, 100)
            # Increase player score by 10
            score += 10

    # Display player score on screen
    textImage = font.render("Score : " + str(score), True, (0, 0, 0))
    screen.blit(textImage, (100, 100))
    
    # Update screen after every frame
    pygame.display.update()





