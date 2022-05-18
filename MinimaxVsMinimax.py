from doctest import DONT_ACCEPT_BLANKLINE
from isolationEnv import *
from helper_function import *
from time import sleep
from GUI import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
board_game = np.ones((SHAPE[1], SHAPE[0])) * (FREE)
board_game[POS['ACTIVE_P1'][0]][POS['ACTIVE_P1'][1]] = ACTIVE_P1
board_game[POS['ACTIVE_P2'][0]][POS['ACTIVE_P2'][1]] = ACTIVE_P2

if __name__ == "__main__":
    env = iMinimaxVSMinimax(5)
    for i in range(0, len(dx)):
        if (POS['ACTIVE_P1'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P1'][1] +dy[i] in range(0, SHAPE[1]) and board_game[POS['ACTIVE_P1'][0] +dx[i]][POS['ACTIVE_P1'][1] +dy[i]] == FREE):
            POS['VALID'].append([POS['ACTIVE_P1'][0] +dx[i], POS['ACTIVE_P1'][1] +dy[i]])
    for ep in range(1):
        depth1 = int(input('depth for maximizer: '))
        depth2 = int(input('depth for minimizer: '))
        player = 1
        done = False
        env.reset(depth1,depth2)
        
        print("START ISOLATION")
        
        while not ENDGAME[0]:
            state,reward,done = env.step()
            if done:
                ENDGAME[0] = True
            # print_board(env.board)
            a = Gui(state, [], True)
            a.display()
            if (ENDGAME[0]):
                time.sleep(5)
            else:
                time.sleep(1)
        # if reward > 0:
        #     print("player1 WON!!!: ",reward)
        # elif reward < 0:
        #     print("player2 WON!!!: ",reward)
        # else:
        #     print("GAME TIE!!!")
        
        print("log out")