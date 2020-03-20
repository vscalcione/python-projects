## Snake game developed in Python by Scalcione Vincenzo

import pygame, sys, random, time, pickle, platform, numpy, os.path
from pygame.locals import *

import pygame.ftfont
from pygame.locals import *

pygame.init()

## Define setup

## Set fps, font e volume of the game ##
fps = 60
fps_clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 24)
game_volume = 0.2

## Define game colors (RGB hex values) ##
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)

## Define width, heigth and title of the window ##
widthSize = 555
heigthSize = 404
surface = pygame.display.set_mode((widthSize, heigthSize))
pygame.display.set_caption("Snake Game")

## Definition of all images used in the game
wallpaper = pygame.image.load("images/wallpaper.png") ## wallpaper image
gameover_image = pygame.image.load("images/gameover.png") ##gameover image
new_record = pygame.image.load("images/new-record.png") ##new record image
apple = pygame.image.load("images/apple.png") ##apple image
skull = pygame.image.load("images/skull.png") ##enemy image
halfed_tail = pygame.image.load("images/halfed-tail.png") ##halfed_tail image
pause_game = pygame.image.load("images/pause.png") ##pause image
icon = pygame.image.load("images/snake_pygame-icon.png") ##icon image
pygame.display.set_icon(icon)

## Creation of snake object
snake = pygame.Surface((14, 14))
snake_head = pygame.Surface((14, 14))
snake.fill(DARK_GREEN)
snake_head.fill(GREEN)

## The log files's configuration changes according to the OS in use (Windows, Linux)
OS = platform.system()
if OS == "Linux":
    from xdg import BaseDirectory

    path_data = BaseDirectory.save_config_path("snake-game/") ##set path for log file
    
    ##if the game folder containing the record does not exist, I create it and also create the record.txt file by setting the record to 0 ##
    if not os.path.exists(path_data):
        os.mkdir(path_data) ##if the directory not exists, create dir
elif OS == "Windows": ##the same precedure used for Linux OS
    path_data = os.path.expanduser("~\\") + "snake_pygame\\"
    if not os.path.exists(path_data):
        os.mkdir(path_data)
else: ## for others OS, create directory into game dir
    path_data = ("Record/")
if not os.path.exists(path_data):
    os.mkdir(path_data)


def initialization():
    ## Definition of all variables that are used
    global game_volume, points, snake_x, snake_y, min, max_x, max_y, direction, previous_direction, difficult, record, bonus_icon, bonus_x, bonus_y

    try:
        record_file = open(path_data + "record.txt", "r") ## open file "record.txt" in read mode and assign it at variable record
    except:
        record_file = open(path_data + "record.txt", "w") ## if this file not exists, create file with record value to 0
        record_file.write("0")
        record_file.close()
        record_file = open(path_data + "record.txt", "r")

    record = int(record_file.read())
    record_file.close()
    pygame.mixer.init()
    pygame.mixer.music.load("sound/music.ogg")
    pygame.mixer.music.set_volume(game_volume)
    pygame.mixer.music.play(-1)
    points = 0
    snake_x = [180, 165, 150, 135, 120, 105]
    snake_y = [180] * 6
    min = 30
    max_x = 525
    max_y = 375
    previous_direction = direction = "right"
    difficult = 0.05
    defineObjects(snake_x[0], snake_y[0])
    bonus_icon = '0'
    bonus_y = 800
    bonus_x = bonus_y

def defineObjects(snake_x, snake_y):
    global apple_x, apple_y, skull_x, skull_y, bonus_x, bonus_y
    apple_x = 15 * (random.randint((min  / 15), ((max_y / 15) - 1)))
    apple_y = 15 * (random.randint((min / 15), ((max_y / 15) - 1 )))
    skull_x = 15 * (random.randint((min / 15), ((max_x / 15) - 1)))
    skull_y = 15 * (random.randint((min / 15), ((max_y / 15) - 1)))

    while (((skull_x >= snake_x - 90 and skull_x <= snake_x + 90) and (skull_y >= snake_y - 90 and skull_y <= snake_y + 90)) or (skull_x == apple_x and skull_y == apple_y)):
        skull_x = 15 * (random.randint((min / 15), ((max_x / 15) - 1)))
        skull_y = 15 * (random.randint((min / 15), ((max_y / 15) - 1)))

    generateNumeber = random.randint(1, 40)
    if generateNumeber == 1:
        bonus_x = 15 * (random.randint((min / 15), ((max_x / 15) - 1)))
        bonus_y = 15 * (random.randint((min / 15), ((max_y / 15) - 1)))

        while ((bonus_x == skull_x and bonus_y == skull_y) or (bonus_x == apple_x and bonus_y == apple_y)):
            bonus_x = 15 * (random.randint((min / 15), ((max_x / 15) - 1)))
            bonus_y = 15 * (random.randint((min / 15), ((max_y / 15) - 1)))
    else:
        bonus_x = bonus_y = 800

def show():
    global direction
    pygame.font.init()
    score = game_font.render('Score: %d' % (points), True, WHITE)
    highscore = game_font.render('Record: %d' % (record), True, WHITE)
    vol = game_font.render('Volume: %d' % (game_volume * 5), True, WHITE)
    bonus = game_font.render('Bonus: [      ]', True, WHITE)
    surface.blit(wallpaper, (0, 0))
    surface.blit(score, (30, 8))
    surface.blit(highscore, (430, 8))
    surface.blit(vol, (30, 382))
    surface.blit(bonus, (430, 382))
    for i in range(1, len(snake_x)):
        surface.blit(snake, (snake_x[i], snake_y[i]))
    surface.blit(snake_head, (snake_x[0], snake_y[0]))
    surface.blit(apple, (apple_x, apple_y))
    surface.blit(skull, (skull_x, skull_y))
    surface.blit(halfed_tail, (bonus_x, bonus_y))
    if bonus_icon == '1':
        surface.blit(halfed_tail, (500, 384))
    pygame.display.update()
    fps_clock.tick(fps)


def write():
    record_file = open(path_data + "record.txt", "w")
    record_file.write(str(int(points)))
    record_file.close()
    surface.blit(new_record, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.key == K_r:
            initialization()
        elif event.key == K_ESCAPE:
            gameOver()

def pauseGame():
    surface.blit(pause_game, (0, 0))
    pygame.display.update()

def restart():
    pygame.mixer.music.stop()
    if points > record:
        write()
    else:
        surface.blit(gameover_image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                gameOver()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    initialization()
                elif event.key == K_ESCAPE:
                    gameOver()

def gameOver():
    pygame.quit()
    sys.exit()


initialization()
while True:
    if points < 10:
        difficult = 0.05
    elif points < 30:
        difficult = 0.045
    elif points < 50:
        difficult = 0.04
    elif points < 80:
        difficult = 0.035
    elif points > 80:
        difficult = 0.03

    increase_points = 1 + round(points * difficult)
    time.sleep(difficult)
    show()
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver()
        elif event.type == KEYDOWN:
            if((((event.key == K_RIGHT or event.key == K_d) and direction != "left") and direction != "gameover") and direction != '0'):
                if changed_position == '1':
                    direction = 'right'
                    previous_direction = direction
                    changed_position = '0'

            elif ((((event.key == K_LEFT or event.key == K_a) and direction != 'right') and direction != 'gameover') and direction != '0'):
                if changed_position == '1':
                    direction = 'left'
                    previous_direction = direction
                    changed_position = '0'

            elif ((((event.key == K_DOWN or event.key == K_s) and direction != 'up') and direction != 'gameover') and direction != '0'):
                if changed_position == '1':
                    direction = 'down'
                    previous_direction = direction
                    changed_position = '0'

            elif ((((event.key == K_UP or event.key == K_w) and direction != 'down') and direction != 'gameover') and direction != '0'):
                if changed_position == '1':
                    direction = 'up'
                    previous_direction = direction
                    changed_position = '0'

            elif (event.key == K_p and direction != 'gameover'):
                if direction == '0':
                    direction = previous_direction
                else:
                    direction = '0'

            elif event.key == K_KP_PLUS or event.key == K_PLUS:
                if volume < 1.0:
                    volume += 0.2  # alzo il volume
                elif volume > 1.0:
                    volume = 1.0
                pygame.mixer.music.set_volume(volume)

            elif event.key == K_KP_MINUS or event.key == K_MINUS:  # controllo se viene premuto il tasto - della tastiera o del numpad
                if game_volume > 0.0:
                    game_volume -= 0.2
                elif game_volume < 0.0:
                    game_volume = 0.0
                pygame.mixer.music.set_volume(game_volume)

            elif event.key == K_ESCAPE:
                gameOver()

            elif event.key == K_r:
                initialization()

            elif (event.key == K_SPACE and bonus_icon == '1' and direction != 'gameover' and direction != '0'):
                bonus_icon = '0'
                i = (len(snake_x) - 1)
                half_snake = (i / 2)
                while half_snake < i:
                    del snake_x[i]
                    i -= 1

    if direction == '0':
        pauseGame()

    elif direction == 'gameover':
        restart()

    else:
        i = len(snake_x) - 1
        while i > 0:
            snake_x[i] = snake_x[i - 1]
            snake_y[i] = snake_y[i - 1]
            i -= 1

        if direction == 'right':
            snake_x[0] += 15
            changed_position = '1'
        elif direction == 'left':
            snake_x[0] -= 15
            changed_position = '1'
        elif direction == 'down':
            snake_y[0] += 15
            changed_position = '1'
        elif direction == 'up':
            snake_y[0] -= 15
            changed_position = '1'

        i = len(snake_x) - 1
        if snake_x[0] == apple_x and snake_y[0] == apple_y:
            points += increase_points
            defineObjects(snake_x[0], snake_y[0])
            snake_x.append(800)
            snake_y.append(800)

        if snake_x[0] == bonus_x and snake_y[0] == bonus_y:
            bonus_icon = '1'
            points += 5 + round(points * difficult)
            defineObjects(snake_x[0], snake_y[0])
            bonus_x = bonus_y = 800
            snake_x.append(800)
            snake_y.append(800)

        if snake_x[0] == skull_x and snake_y[0] == skull_y:
            direction = 'gameover'

        while i > 4:
            if snake_x[0] == snake_x[i] and snake_y[0] == snake_y[i]:
                direction = 'gameover'
            i -= 1

        if ((snake_x[0] >= max_x) or (snake_x[0] < min) or (snake_y[0] >= max_y) or (snake_y[0] < min)):
            direction = 'gameover'
