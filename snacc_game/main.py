import pygame
from constants import *
import random
import time


# Just some stuff pygame needs
def pygame_init():
    # Initialize all of the pygame modules
    pygame.init()
    # Initialize a clock the we can use later
    clock = pygame.time.Clock()
    # Initialize the screen with its size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    # Setting the Surface of the game screen according to the screen screen we've created
    game_screen = pygame.Surface(screen.get_size())
    # Converting the game screen to a pixels
    game_screen.convert()

    return clock, screen, game_screen


# Draw on screen a rectangle for every snake square
def draw_snake(game_screen, snake_locations):
    for loc in snake_locations:
        # The game screen, X, Y, Width, Height
        pygame.draw.rect(game_screen, SNAKE_COLOR, (loc[0] * GRID_SIZE, loc[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

def move_snake(snake_dir, snake_locations):

    old_head = snake_locations[0] # tuple
    print(f"snake_dir[0] = {snake_dir[0]}")
    new_head = (old_head[0]+snake_dir[0], old_head[1]+snake_dir[1])
    snake_locations.insert(0, new_head)
    snake_locations.pop()

    return snake_locations

def change_dir(snake_dir):
    # UP = 0, DOWN = 1, RIGHT = 2, LEFT = 3
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not(snake_dir == DIRECTION_DICT["DOWN"]):
                print("up is pressed ye")
                snake_dir = DIRECTION_DICT["UP"]
            elif event.key == pygame.K_s and not(snake_dir == DIRECTION_DICT["UP"]):
                print("down is pressed ye")
                snake_dir = DIRECTION_DICT["DOWN"]
            elif event.key == pygame.K_d and not(snake_dir == DIRECTION_DICT["LEFT"]):
                print("right is pressed ye")
                snake_dir = DIRECTION_DICT["RIGHT"]
            elif event.key == pygame.K_a and not(snake_dir == DIRECTION_DICT["RIGHT"]):
                print("left is pressed ye")
                snake_dir = DIRECTION_DICT["LEFT"]
    return snake_dir

def generate_apple_location(snake_locs):
    apple_y = random.randint(0,SCREEN_HEIGHT/GRID_SIZE-1)
    apple_x = random.randint(0,SCREEN_WIDTH/GRID_SIZE-1)
    apple_loc = (apple_x,apple_y)
    while apple_loc in snake_locs:
        apple_y = random.randint(0, SCREEN_HEIGHT / GRID_SIZE-1)
        apple_x = random.randint(0, SCREEN_WIDTH / GRID_SIZE-1)
        apple_loc = (apple_x, apple_y)
    return apple_loc

def draw_apple(game_screen, apple_loc):
    pygame.draw.rect(game_screen, APPLE_COLOR, (apple_loc[0] * GRID_SIZE, apple_loc[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

def check_eat_apple(apple_loc, snake_locs, snake_dir, game_screen):
    if apple_loc[0] == snake_locs[0][0] and apple_loc[1] == snake_locs[0][1]:
        snake_locs.append(snake_locs[-1][0]+snake_dir[0] and snake_locs[-1][1]+snake_dir[1])
        draw_apple(game_screen,apple_loc)
        return True
    return False

def snake_into_snake(snake_loc): # still misses out some cases ig...
    flagover=False
    for i in range(1,len(snake_loc)-1):
        if snake_loc[0][0] == snake_loc[i][0] and snake_loc[0][1] == snake_loc[i][1]:
            flagover=True
    return flagover


###

def if_pressed_space():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                return True
    return False

def if_pressed_esc():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                pygame.quit()
                return True
    return False

###

def pressed_space_or_esc():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            print("smth pressed")
            if event.key == pygame.K_ESCAPE:
                print("esccccccccccccccccccccccccccccccccccc")
                return "ESCAPE"
            elif event.key == pygame.K_SPACE:
                print("spaceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                return "SPACE"
            else:
                print("nothinggggggggggggggggggggg")
                return "nothing"


def snake_into_borders(snake_loc):
        return snake_loc[0][0] < 0 or snake_loc[0][0] > SCREEN_WIDTH/GRID_SIZE-1 or snake_loc[0][1] < 0 or snake_loc[0][1] > SCREEN_HEIGHT/GRID_SIZE-1

def main():
    clock, screen, game_screen = pygame_init()
    # All of the snake's locations.
    snake_direction = (0,0) # don't move until dir pressed
    snake_locations = [SNAKE_STARTING_LOC]
    player_pressed_esc = False
    game_over = False

    apple_location = generate_apple_location(snake_locations)
    points = 0

    while not player_pressed_esc: # and not game_over
        # Moving the clock
        clock.tick(GAME_SPEED)
        # Creating the current screen
        screen.blit(game_screen, (0, 0))
        # Filing the screen with the color
        game_screen.fill(BACKGROUND_COLOR)
        #
        if not(game_over):
            text_font = pygame.font.Font("upheavtt.ttf", 160)
            text_label = text_font.render(str(points), True, (50, 50, 50))
            game_screen.blit(text_label, (SCREEN_WIDTH / 25, SCREEN_HEIGHT / 3.5))
            # player_pressed_esc = if_pressed_esc()
            apple_eaten = check_eat_apple(apple_location, snake_locations, snake_direction, game_screen)
            if (apple_eaten):
                apple_location = generate_apple_location(snake_locations)
                points += 1
            draw_apple(game_screen, apple_location)
            snake_direction = change_dir(snake_direction)
            snake_locations = move_snake(snake_direction, snake_locations)
            game_over = snake_into_snake(snake_locations) or snake_into_borders(snake_locations)
            draw_snake(game_screen, snake_locations)
        else:
            fontt = pygame.font.Font("upheavtt.ttf", 105)
            label = fontt.render("GAME OVER", True, (200, 50, 50))
            game_screen.blit(label, (SCREEN_WIDTH / 25, SCREEN_HEIGHT / 6))

            text_font = pygame.font.Font("upheavtt.ttf", 160)
            text_label = text_font.render(str(points), True, (100, 100, 100))
            game_screen.blit(text_label, (SCREEN_WIDTH / 25, SCREEN_HEIGHT / 3.5))

            text_labellll = fontt.render("POINTS", True, (50, 50, 50))
            game_screen.blit(text_labellll, (SCREEN_WIDTH / 25, SCREEN_HEIGHT / 2))

            text_font = pygame.font.Font("upheavtt.ttf", 30)
            text_label = text_font.render("To try again press SPACE", True, (30, 30, 30))
            game_screen.blit(text_label, (SCREEN_WIDTH / 25, SCREEN_HEIGHT - 200))

            text_label = text_font.render("To quit, press ESCAPE", True, (30, 30, 30))
            game_screen.blit(text_label, (SCREEN_WIDTH / 25, SCREEN_HEIGHT - 175))

            pygame.display.update()

            # if pressed_space_or_esc() == "ESCAPE" or pressed_space_or_esc() == "SPACE":
            if not pressed_space_or_esc() == "nothing":
                return pressed_space_or_esc()
            # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")

            pygame.display.update()


            # if if_pressed_space():
            #     return True
            # if if_pressed_esc():
            #     pygame.quit()
            # if_pressed_esc()

        # Updating the screen after we've draw something on it
        pygame.display.update()

def loop_main():
    pressed_key = main()
    if pressed_key == "SPACE":
        while pressed_key == "SPACE":
            main()
    elif pressed_key == "ESCAPE":
        pygame.quit()
    pygame.quit()
    # while pressed_space:
    #     main()


# main()
loop_main()
pygame.quit()
