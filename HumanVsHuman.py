from isolationEnv import *
from GUI import *
from parameter import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
board_game = np.ones((SHAPE[1], SHAPE[0])) * (FREE)
board_game[POS['ACTIVE_P1'][0]][POS['ACTIVE_P1'][1]] = ACTIVE_P1
board_game[POS['ACTIVE_P2'][0]][POS['ACTIVE_P2'][1]] = ACTIVE_P2

if __name__ == '__main__':
    #initialize
    env = iHumanVSHuman()
    for i in range(0, len(dx)):
        if (POS['ACTIVE_P1'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P1'][1] +dy[i] in range(0, SHAPE[1]) and board_game[POS['ACTIVE_P1'][0] +dx[i]][POS['ACTIVE_P1'][1] +dy[i]] == FREE):
            POS['VALID'].append([POS['ACTIVE_P1'][0] +dx[i], POS['ACTIVE_P1'][1] +dy[i]])
    done = False
    while not ENDGAME[0]:
        # updateGame()
        state, reward, done = env.step()  
        if done:
            ENDGAME[0] = True
        a = Gui(state)
        # print(state)
        a.display()
        
        if (ENDGAME[0]):
            time.sleep(5)
    