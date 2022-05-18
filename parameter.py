#STATE:
FREE = 0
BLOCK = 2
ACTIVE_P1 = 1 #component
ACTIVE_P2 = -1 #component
ACTIVE = {1 : ACTIVE_P1, -1 : ACTIVE_P2}

#cell neighbor position
dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]

#hyper_parameter
# WIDTH = 6
EDGE = 120
SHAPE = (6, 6)
WIDTH = SHAPE[0] * EDGE
HEIGHT = SHAPE[1] * EDGE
ENDGAME = [False]
MARGIN = 2
OFFSET = 50


#left_direction
L_DIRECTION = [(-1,0),(-1,1),(-1,-1)]
R_DIRECTION = [(1,0),(1,1),(1,-1)]
U_DIRECTION = [(-1,1),(0,1),(1,1)]
D_DIRECTION = [(-1,-1),(0,-1),(1,-1)]

DIRECTION = {
    "left" : L_DIRECTION,
    "right" : R_DIRECTION,
    "up" : U_DIRECTION,
    "down" : D_DIRECTION
}

DIRECTION_LABEL = ["left","right","up","down"]

#color for display GUI python
blue = (104, 149, 197)
black = (0, 0, 0)
white = (255,255,255)
red = (255,69,0)
yellow = (255,255,0)
blue_second = (130,202,250)
red_first = (244,41,65)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Position for
POS = {'ACTIVE_P1': [0, int((SHAPE[1] - 1) / 2)], 
        'ACTIVE_P2': [SHAPE[0] - 1, int((SHAPE[1] + 1) / 2)], 
        'VALID': [],
        'SELECT' : [-1,-1]
} # [row,col]
TURN = [0]

