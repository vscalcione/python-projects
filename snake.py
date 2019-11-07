import pygame, sys, time, pickle, platform, numpy, random, os.path, pygame.ftfont
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 134, 139)
LIGHTBLUE  = (0, 255, 255)

pygame.init()



def setup():
    displayWidth = 800
    displayHeigth = 600
    displayGameHeigth = displayHeigth - 100

    gameDisplay = pygame.display.set_mode((displayWidth, displayHeigth))
    pygame.display.set_caption("Snake Game v 0.1")

    iconGame = pygame.image.load("Images/v 0.1/apple.png")
    pygame.display.set_icon(iconGame)

    backgroundImage = pygame.image.load("Images/v 0.1/background.jpg")
    headImage = pygame.image.load("Images/v 0.1/snakeHead.png")
    appleImage = pygame.image.load("Images/v 0.1/apple.png")
    bodyImage = pygame.image.load("Images/v 0.1/snakeBody.png")

    clock = pygame.time.Clock()
    snakeSize = 20
    fps = 15
    appleThickness = 20

def setBackgroundButtons():
    button("Start Game", 70, 530, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action = "start")

def