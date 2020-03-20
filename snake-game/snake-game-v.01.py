import pygame, sys, time, pickle, platform, numpy, random, os.path
from pygame.locals import *

import pygame.ftfont
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 134, 139)
LIGHTBLUE = (0, 255, 255)

pygame.init()
display_width = 800
display_height = 600
display_game_height = display_height - 100

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# Set Icon
icon = pygame.image.load("images/v 0.1/apple.png")
pygame.display.set_icon(icon)

# images
background_image = pygame.image.load("images/v 0.1/background.jpg")  # 800px x 600px
head_image = pygame.image.load("images/v 0.1/snakeHead.png")  # 20px x 20px
apple_image = pygame.image.load("images/v 0.1/apple.png")  # 20px x 20px
body_image = pygame.image.load("images/v 0.1/snakeBody.png")  # 20px x 20px

# Clock for frames, snake size, frame per sec, apple size, direction
clock = pygame.time.Clock()
snake_size = 20
fps = 15
apple_thickness = 20


def set_background_buttons():
    button("Start Game", 70, 530, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="start")
    button("Help", 70, 560, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="help")
    button("pause/play", 630, 530, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="pause/play")
    button("Quit", 630, 560, 90, 20, LIGHTBLUE, DARKBLUE, WHITE, action="quit")


def game_intro():
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
        game_display.blit(background_image, (0, 0))
        message_to_screen("Welcome to Snake", WHITE, -100, 80)
        message_to_screen("The objective of the game is to eat the apples", WHITE, -30)
        message_to_screen("The more apples you eat the longer you get", WHITE, 10)
        message_to_screen("If you run into yourself or the edges, you die!", WHITE, 50)
        message_to_screen("Press C to play, P to pause, or Q to quit", WHITE, 180)
        set_background_buttons()
        pygame.display.update()
        clock.tick(15)


def text_objects(text, color, size):
    # Font
    pygame.font.init()
    game_font = pygame.font.Font(None, 24)
    text_surface = game_font.render(text, True, WHITE)

    # Text surface, and text rectangle (return tuple)
    return text_surface, text_surface.get_rect()


def button(text, x, y, width, height, inactive_color, active_color, text_color=BLACK, action=None):
    # Get mouse position
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(game_display, active_color, (x, y, width, height))

        if click[0] == 1 and action is not None:
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
        pygame.draw.rect(game_display, inactive_color, (x, y, width, height), 2)

    text_to_button(text, text_color, x, y, width, height)


def text_to_button(msg, color, button_x, button_y, button_width, button_height, size=16):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    game_display.blit(text_surf, text_rect)


def message_to_screen(msg, color, y_displace=0, size=25):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_game_height / 2) + y_displace
    game_display.blit(text_surf, text_rect)


def check_rand_app_loc(snake_list, rand_apple_x, rand_apple_y):
    invalid = False

    for xNy in snake_list:
        if xNy[0] == rand_apple_x and xNy[1] == rand_apple_y:
            invalid = True

    return invalid


def rand_apple_gen(snake_list, display_game_heigth=display_game_height):
    # Don't put the apple where the snake is
    invalid = True

    while invalid:
        rand_apple_x = round(random.randrange(0, display_width - apple_thickness) / 20.0) * 20.0
        rand_apple_y = round(random.randrange(0, display_game_heigth - apple_thickness) / 20.0) * 20.0
        invalid = check_rand_app_loc(snake_list, rand_apple_x, rand_apple_y)

    return rand_apple_x, rand_apple_y


def snake(snake_size, snake_list):
    # Rotate the head of the snake (actually moves counter clockwise)
    if direction == "right":
        head = pygame.transform.rotate(head_image, 270)

    elif direction == "left":
        head = pygame.transform.rotate(head_image, 90)

    elif direction == "up":
        head = head_image

    elif direction == "down":
        head = pygame.transform.rotate(head_image, 180)

    # Draw head of the snake
    game_display.blit(head, (snake_list[-1][0], snake_list[-1][1]))

    # 2 element list (everythinge except the last element - head)
    for xNy in snake_list[:-1]:
        game_display.blit(body_image, (xNy[0], xNy[1], snake_size, snake_size))


def score(score):
    message_to_screen("SCORE", WHITE, 290, 30)
    message_to_screen(str(score), WHITE, 320, 25)


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

        game_display.blit(background_image, (0, 0))
        message_to_screen("PAUSED", WHITE, -100, 100)
        message_to_screen("Press C to continue or Q to quit.", WHITE, 25)

        set_background_buttons()

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


def gameLoop(display_game_height=display_game_height):
    # Exit the entire game and when gameover
    game_exit = False
    game_over = False

    global direction
    direction = "right"

    # Snake x and y position. The speed (movement) of the snake x & y position
    lead_snake_x = round((display_width / 2) / 20.0) * 20.0
    lead_snake_y = round((display_game_height / 2) / 20.0) * 20.0
    lead_change_x = 20
    lead_change_y = 0

    # Snake List (all parts of the snake)
    snake_list = []
    snake_length = 1

    # Call random apple generator
    rand_apple_x, rand_apple_y = rand_apple_gen(snake_list)

    # Game Exit to exit entire game
    while not game_exit:

        # Check if the game is over or not
        if game_over:
            message_to_screen("GAME OVER", WHITE, -100, 100)
            message_to_screen("Press C to continue or Q to quit.", WHITE, 25)
            pygame.display.update()

            # Keep looping game over until get valid input (quit game or continue)
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_exit = True
                        game_over = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_exit = True
                            game_over = False

                        if event.key == pygame.K_c:
                            gameLoop()

        # Game Exit check keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_change_x = -snake_size
                    lead_change_y = 0

                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_change_x = snake_size
                    lead_change_y = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_change_x = 0
                    lead_change_y = -snake_size

                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_change_x = 0
                    lead_change_y = snake_size

                elif event.key == pygame.K_p:
                    pause()

        # Check game boundaries
        if (lead_snake_x >= display_width or lead_snake_x < 0 or
                lead_snake_y >= display_game_height or lead_snake_y < 0):
            game_over = True

        if not game_over:
            # Movement of snake (the speed)
            lead_snake_x += lead_change_x
            lead_snake_y += lead_change_y

            # Display the background
            game_display.blit(background_image, (0, 0))

            # Display the random apple
            game_display.blit(apple_image, (rand_apple_x, rand_apple_y))

            # Add snake head position to snake head. Then add the snake head to head of snake list
            snake_head = []
            snake_head.append(lead_snake_x)
            snake_head.append(lead_snake_y)
            snake_list.append(snake_head)

            # Only draw snake list (dont draw extra snake length)
            if len(snake_list) > snake_length:
                del snake_list[0]

            # Check if snake head collides into itself
            for eachSegment in snake_list[:-1]:
                if eachSegment == snake_head:
                    game_over = True

            # Call the snake function to draw the snake onto the screen
            snake(snake_size, snake_list)

            # Call score function to display the current score
            score(snake_length - 1)

            set_background_buttons()

            # Update the entire screen
            pygame.display.update()

            # Check if ate apple
            if (lead_snake_x >= rand_apple_x and lead_snake_x < rand_apple_x + apple_thickness or
                    lead_snake_x + snake_size > rand_apple_x and
                    lead_snake_x + snake_size < rand_apple_x + apple_thickness):

                if (lead_snake_y >= rand_apple_y and lead_snake_y < rand_apple_y + apple_thickness):
                    rand_apple_x, rand_apple_y = rand_apple_gen(snake_list)
                    snake_length += 1

                elif (lead_snake_y + snake_size > rand_apple_y and
                      lead_snake_y + snake_size < rand_apple_y + apple_thickness):
                    rand_apple_x, rand_apple_y = rand_apple_gen(snake_list)
                    snake_length += 1

            # Add the speed
            clock.tick(fps)

    pygame.quit()
    quit()


# Main Starts here. gall function
game_intro()
gameLoop()
