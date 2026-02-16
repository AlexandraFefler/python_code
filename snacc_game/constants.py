SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
GRID_SIZE = 25 # x<0, x>gridsize
# 500/10 = every mishbecet is 50 px

GAME_SPEED = 10

BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 204, 0)
APPLE_COLOR = (204, 0, 0)

# SNAKE_STARTING_LOC = (SCREEN_WIDTH/GRID_SIZE/2-1, SCREEN_HEIGHT/GRID_SIZE/2-1) #(x,y)
SNAKE_STARTING_LOC = (15,15) #(x,y)

# DIRECTION_DICT = {"UP":{"x":0,"y":-1}},{"DOWN":{"x":0,"y":1}},{"RIGHT":{"x":1,"y":0}},{"LEFT":{"x":-1,"y":0}} # DIRECTION_DICT["UP"]["x"] - for ex.
DIRECTION_DICT = {"UP":(0,-1),"DOWN":(0,1),"RIGHT":(1,0),"LEFT":(-1,0)} #DIRECTION_DICT["UP"][0] - ex. for (X,y)
