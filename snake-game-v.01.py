import pygame, sys, time, pickle, platform, numpy, random, os.path
from pygame.locals import *

import pygame.ftfont
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 134, 139)
LIGHTBLUE = (0, 255, 255)

pygame.init()
displayWidth = 800
displayHeigth = 600
displayGameHeigth = displayHeigth - 100

gameDisplay = pygame.display.set_mode((displayWidth, displayHeigth))
pygame.display.set_caption("Snake Game")

# Set Icon
icon = pygame.image.load("Images/v 0.1/apple.png")
pygame.display.set_icon(icon)

# Images
backgroundImage = pygame.image.load("Images/v 0.1/background.jpg")  # 800px x 600px
headImage = pygame.image.load("Images/v 0.1/snakeHead.png")  # 20px x 20px
appleImage = pygame.image.load("Images/v 0.1/apple.png")  # 20px x 20px
bodyImage = pygame.image.load("Images/v 0.1/snakeBody.png")  # 20px x 20px

# Clock for frames, snake size, frame per sec, apple size, direction
clock = pygame.time.Clock()
snakeSize = 20
fps = 15
appleThickness = 20


def setBackgroundButtons():
    button("Start Game", 70, 530, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="start")
    button("Help", 70, 560, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="help")
    button("pause/play", 630, 530, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="pause/play")
    button("Quit", 630, 560, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="quit")


def gameIntro():
    intro = True

    # Keep display the intro while the user has not exited or continued
    while intro:
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # Continue snake game
                if event.key == pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # Display background and rules to user
        gameDisplay.blit(backgroundImage, (0, 0))
        messageToScreen("Welcome to Snake", WHITE, -100, 80)
        messageToScreen("The objective of the game is to eat the apples", WHITE, -30)
        messageToScreen("The more apples you eat the longer you get", WHITE, 10)
        messageToScreen("If you run into yourself or the edges, you die!", WHITE, 50)
        messageToScreen("Press C to play, P to pause, or Q to quit", WHITE, 180)
        setBackgroundButtons()
        pygame.display.update()
        clock.tick(15)

def textObjects(text, color, size):
    # Font
    pygame.font.init()
    gameFont = pygame.font.Font(None, 24)
    textSurface = gameFont.render(text, True, WHITE)

    # Text surface, and text rectangle (return tuple)
    return textSurface, textSurface.get_rect()



def button(text, x, y, width, height, inactiveColor, activeColor, textColor=BLACK, action=None):
    # Get mouse position
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x, y, width, height))

        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "pause/play":
                pause()

            if action == "start":
                gameLoop()

            if action == "help":
                pass
    else:
        # pygame.draw.circle(gameDisplay, inactiveColor, (x, y), width)
        pygame.draw.rect(gameDisplay, inactiveColor, (x, y, width, height), 2)

    textToButton(text, textColor, x, y, width, height)


def textToButton(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size=16):
    textSurf, textRect = textObjects(msg, color, size)
    textRect.center = ((buttonX + (buttonWidth / 2)), buttonY + (buttonHeight / 2))
    gameDisplay.blit(textSurf, textRect)


def messageToScreen(msg, color, yDisplace=0, size=25):
    textSurf, textRect = textObjects(msg, color, size)
    textRect.center = (displayWidth / 2), (displayGameHeigth / 2) + yDisplace
    gameDisplay.blit(textSurf, textRect)


def checkRandAppLoc(snakeList, randAppleX, randAppleY):
    invalid = False

    for xNy in snakeList:
        if xNy[0] == randAppleX and xNy[1] == randAppleY:
            invalid = True

    return invalid


def randAppleGen(snakeList, displayGameHeight=displayGameHeigth):
    # Don't put the apple where the snake is
    invalid = True

    while invalid:
        randAppleX = round(random.randrange(0, displayWidth - appleThickness) / 20.0) * 20.0
        randAppleY = round(random.randrange(0, displayGameHeight - appleThickness) / 20.0) * 20.0
        invalid = checkRandAppLoc(snakeList, randAppleX, randAppleY)

    return randAppleX, randAppleY



def snake(snakeSize, snakeList):
    # Rotate the head of the snake (actually moves counter clockwise)
    if direction == "right":
        head = pygame.transform.rotate(headImage, 270)

    elif direction == "left":
        head = pygame.transform.rotate(headImage, 90)

    elif direction == "up":
        head = headImage

    elif direction == "down":
        head = pygame.transform.rotate(headImage, 180)

    # Draw head of the snake
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    # 2 element list (everythinge except the last element - head)
    for xNy in snakeList[:-1]:
        gameDisplay.blit(bodyImage, (xNy[0], xNy[1], snakeSize, snakeSize))




def score(theScore):
    messageToScreen("SCORE", WHITE, 290, 30)
    messageToScreen(str(theScore), WHITE, 320, 25)


"""
------------------------------------------------------------------------------------------
pause
------------------------------------------------------------------------------------------
This function allows the user to pause the game

Returns: nothing (pauses the game until unpaused)
------------------------------------------------------------------------------------------
"""


def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.blit(backgroundImage, (0, 0))
        messageToScreen("PAUSED", WHITE, -100, 100)
        messageToScreen("Press C to continue or Q to quit.", WHITE, 25)

        setBackgroundButtons()

        pygame.display.update()
        clock.tick(5)


"""
------------------------------------------------------------------------------------------
gameLoop
------------------------------------------------------------------------------------------
This function is basically the structure of the entire game. The entire snake game
will be running until the user decides to exit the game.

Returns: nothing (keep playing snake until exit)
------------------------------------------------------------------------------------------
"""


def gameLoop(displayGameHeight=displayGameHeigth):
    # Exit the entire game and when gameover
    gameExit = False
    gameOver = False

    global direction
    direction = "right"

    # Snake x and y position. The speed (movement) of the snake x & y position
    leadSnakeX = round((displayWidth / 2) / 20.0) * 20.0
    leadSnakeY = round((displayGameHeight / 2) / 20.0) * 20.0
    leadChangeX = 20
    leadChangeY = 0

    # Snake List (all parts of the snake)
    snakeList = []
    snakeLength = 1

    # Call random apple generator
    randAppleX, randAppleY = randAppleGen(snakeList)

    # Game Exit to exit entire game
    while not gameExit:

        # Check if the game is over or not
        if gameOver == True:
            messageToScreen("GAME OVER",
                            WHITE,
                            -100,
                            100)
            messageToScreen("Press C to continue or Q to quit.",
                            WHITE,
                            25)
            pygame.display.update()

            # Keep looping game over until get valid input (quit game or continue)
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False

                        if event.key == pygame.K_c:
                            gameLoop()

        # Game Exit check keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    leadChangeX = -snakeSize
                    leadChangeY = 0

                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    leadChangeX = snakeSize
                    leadChangeY = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    leadChangeX = 0
                    leadChangeY = -snakeSize

                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    leadChangeX = 0
                    leadChangeY = snakeSize

                elif event.key == pygame.K_p:
                    pause()

        # Check game boundaries
        if (leadSnakeX >= displayWidth or leadSnakeX < 0 or
                leadSnakeY >= displayGameHeight or leadSnakeY < 0):
            gameOver = True

        if not gameOver:
            # Movement of snake (the speed)
            leadSnakeX += leadChangeX
            leadSnakeY += leadChangeY

            # Display the background
            gameDisplay.blit(backgroundImage, (0, 0))

            # Display the random apple
            gameDisplay.blit(appleImage, (randAppleX, randAppleY))

            # Add snake head position to snake head. Then add the snake head to head of snake list
            snakeHead = []
            snakeHead.append(leadSnakeX)
            snakeHead.append(leadSnakeY)
            snakeList.append(snakeHead)

            # Only draw snake list (dont draw extra snake length)
            if len(snakeList) > snakeLength:
                del snakeList[0]

            # Check if snake head collides into itself
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True

            # Call the snake function to draw the snake onto the screen
            snake(snakeSize, snakeList)

            # Call score function to display the current score
            score(snakeLength - 1)

            setBackgroundButtons()

            # Update the entire screen
            pygame.display.update()

            # Check if ate apple
            if (leadSnakeX >= randAppleX and leadSnakeX < randAppleX + appleThickness or
                    leadSnakeX + snakeSize > randAppleX and
                    leadSnakeX + snakeSize < randAppleX + appleThickness):

                if (leadSnakeY >= randAppleY and leadSnakeY < randAppleY + appleThickness):
                    randAppleX, randAppleY = randAppleGen(snakeList)
                    snakeLength += 1

                elif (leadSnakeY + snakeSize > randAppleY and
                      leadSnakeY + snakeSize < randAppleY + appleThickness):
                    randAppleX, randAppleY = randAppleGen(snakeList)
                    snakeLength += 1

            # Add the speed
            clock.tick(fps)

    pygame.quit()
    quit()


# Main Starts here. gall function
gameIntro()
gameLoop()

