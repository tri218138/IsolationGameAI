from interface_game.environment import *
from Minimax_Interface_Isolation import *
import copy
from Minimax_Isolation import *
import time

# class iMinimaxVsMinmax_v1(BaseEnvironment):
#     def __init__(self):
#         self.depth = {-1 : 0, 1 : 0}
#         self.current_turn = 1
#         self.env = None
#         self.board = None
        
#     def reset(self,depth1 = 4,depth2 = 5):
#         self.depth = {-1 : depth1, 1 : depth2}
#         self.board = MinimaxII(max(depth1, depth2),{}).getBoard()
#         return self.board.copy()
    
#     def env_act(self):
#         pass
    
#     def check_win(self):
#         return self.env.check_win(self.board,self.current_turn)

#     def step(self):
#         turn = self.current_turn
        
#         self.env = MinimaxII(self.depth[turn],{})
#         self.env.minimax_act(self.board,turn)
#         reward,done = self.check_win()
        

#         self.current_turn = turn * -1
#         return self.board.copy(),reward,done
        
class iMinimaxVSMinimax(BaseEnvironment):
    def __init__(self,depth,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.player_mark = 1
        self.path = path

    # def env_act(self):
    #     old,new = self.env.aimove(self.env.board,self.current_turn)
    #     reward,done = self.check_win()
    #     self.current_turn = -1 * self.current_turn
    #     return reward,done

    def reset(self,depth1,depth2):
        self.env = MinimaxIsolation(max(depth1,depth2),None)
        self.board = self.env.board
        # self.player_mark = 1
        return copy.deepcopy(self.board)
    
    def action(self):
        pass
    
    def get_act_space(self,board,player):
        player_pos = self.env.get_pos(board,player)
        new_space = self.env.get_all_empty_cell(board,player_pos[0],player_pos[1])
        
        action_space = [(player_pos,cell) for cell in new_space]
        return action_space
        
    def sample_act(self,board,player):
        action_space = self.get_act_space(board,player)
        cell = random.choice(action_space)
        
        old,new = cell
        self.env.move_piece(board,player,old,new)
        # self.board = board
        board = self.env.board.copy()
        return old,new
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
    
    def step(self):
        old, new = None, None
        if self.env.MINIMAX_DEPTH != 0:
            old,new = self.env.aimove(self.env.board,self.current_turn)
            # POS['ACTIVE_P2'] = copy.deepcopy(new)
        else:
            old,new = self.sample_act(self.env.board,self.current_turn)
        # self.env.move_piece(self.env.board,self.current_turn,old,new)
        self.board = self.env.board
        reward,done = self.check_win()
        if self.current_turn == 1:
            POS['ACTIVE_P2'] = copy.deepcopy(new)
        else:
            POS['ACTIVE_P1'] = copy.deepcopy(new)
        self.current_turn = -1 * self.current_turn
        # if done:
            # return copy.deepcopy(self.board), reward, done
        # reward,done = self.env_act()
        return copy.deepcopy(self.board),reward,done
    
class iMinimaxVSHuman(BaseEnvironment):
    def __init__(self,depth,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.player_mark = 1
        self.path = path

    def print_board(self):
        self.env.print_board(self.board)

    def env_act(self):
        old,new = self.env.aimove(self.env.board,self.current_turn)
        # print(old)
        # print(new)
        POS['ACTIVE_P2'] = copy.deepcopy(new)
        reward,done = self.check_win()
        # self.current_turn = -1 * self.current_turn
        return reward,done
     
    def reset(self,player,depth,path):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1 #player turn
        self.player_mark = player
        return copy.deepcopy(self.board)
    def step(self):        
        if self.env.get_player_piece(self.board,self.current_turn) == 0:
            return copy.deepcopy(self.board),8 * -self.current_turn,True
        if TURN[0] == 0 or TURN[0] == 1:#player
            POS['VALID'].clear()
            if (TURN[0] == 0):
                for i in range(0, len(dx)):
                    if (POS['ACTIVE_P1'][0] +dx[i] in range(0, SHAPE[0]) and POS['ACTIVE_P1'][1] +dy[i] in range(0, SHAPE[1]) and self.board[POS['ACTIVE_P1'][0] +dx[i]][POS['ACTIVE_P1'][1] +dy[i]] == FREE):
                        POS['VALID'].append([POS['ACTIVE_P1'][0] +dx[i], POS['ACTIVE_P1'][1] +dy[i]])       
            else:
                for r in range(0, SHAPE[0]):
                    for c in range(0, SHAPE[1]):
                        if (self.board[r][c] == FREE and [r, c] != POS['ACTIVE_P1'] and [r, c] != POS['ACTIVE_P2']):
                            POS['VALID'].append([r, c])
            self.env.player_move(self.board,self.current_turn)
            reward,done = self.check_win()
            if (TURN[0] == 2):
                self.current_turn = -1 * self.current_turn
            return copy.deepcopy(self.board), reward, done
        else:
            # print(self.board)
            reward,done = self.env_act()
            reward,done = self.check_win()
            # print(self.board)
            TURN[0] = 0
            self.current_turn = -1 * self.current_turn
            time.sleep(0.5)
            return copy.deepcopy(self.board), reward, done
    # def step(self):
    #     if self.current_turn == self.player_mark:
    #         print("here1")
    #         input()
    #         if self.env.get_player_piece(self.board,self.current_turn) == 0:
    #             return copy.deepcopy(self.board),8 * -self.current_turn,True
    #         curTurn = copy.deepcopy(TURN[0])
    #         self.env.player_move(self.board,self.current_turn) 
    #         reward,done = self.check_win()
    #         self.current_turn = -1 * self.current_turn
    #         if done:
    #             return copy.deepcopy(self.board), reward, done
    #         reward,done = self.env_act()
    #         return copy.deepcopy(self.board), reward, done            
    #     else:
    #         print("here2")
    #         input()
    #         if self.env.get_player_piece(self.board,self.current_turn) == 0:
    #             return copy.deepcopy(self.board),8 * -self.current_turn,True
    #         reward,done = self.env_act()
    #         if done:
    #             return copy.deepcopy(self.board), reward, done
    #         self.env.player_move(self.board,self.current_turn) 
    #         reward,done = self.check_win()
    #         self.current_turn = -1 * self.current_turn
    #         return copy.deepcopy(self.board), reward, done                    
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
        
class iHumanVSHuman(BaseEnvironment):
    def __init__(self,depth = 0,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.player_mark = 1
        self.path = path
        
    def env_act(self):
        pass
                
    def print_board(self):
        self.env.print_board(self.board)
        
    def reset(self,player,depth,path):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = player
        self.player_mark = 1
        return copy.deepcopy(self.board)
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
    
    def step(self):
        if self.env.get_player_piece(self.board,self.current_turn) == 0:
            return copy.deepcopy(self.board),8 * -self.current_turn,True
        self.env.player_move(self.board,self.current_turn) 
        reward,done = self.check_win()
        self.current_turn = -1 * self.current_turn
        return copy.deepcopy(self.board),reward,done

class iGenVSMinimax(BaseEnvironment):
    def __init__(self,depth,path={}):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        self.current_turn = 1
        self.igen = 1
        self.path = path

    def reset(self,depth,igen):
        self.env = MinimaxIsolation(depth,None)
        self.board = self.env.board
        # self.player_mark = 1
        self.igen = igen
        return copy.deepcopy(self.board)
    
    def action(self):
        pass
    
    def get_act_space(self,board,player):
        player_pos = self.env.get_pos(board,player)
        new_space = self.env.get_all_empty_cell(board,player_pos[0],player_pos[1])
        
        action_space = [(player_pos,cell) for cell in new_space]
        return action_space
        
    def sample_act(self,board,player):
        action_space = self.get_act_space(board,player)
        cell = random.choice(action_space)
        
        old,new = cell
        board[old[0]][old[1]] = FREE
        board[new[0]][new[1]] = player
        
        # component_action_space = self.get_act_space(board,-player)
        # self.env.move_piece(board,player,old,new)
        # self.board = board
        
        new_comp = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == FREE:
                    new_comp.append((i,j))
        new_comp_rand = random.choice(new_comp)
        board[new_comp_rand[0]][new_comp_rand[1]] = BLOCK
    
        # board = self.env.board.copy()
        return old,new
    
    def check_win(self):
        point,flag = self.env.check_win(self.board,self.current_turn)
        return point,flag
    
    def step(self):
        old, new = None, None
        if self.igen == self.current_turn: #gen move first
            old,new = self.sample_act(self.env.board,self.current_turn)
        else:
            old,new = self.env.aimove(self.env.board,self.current_turn)
        if self.current_turn == 1:
            POS['ACTIVE_P1'] = copy.deepcopy(new)
        else:
            POS['ACTIVE_P2'] = copy.deepcopy(new)
        self.board = self.env.board
        reward,done = self.check_win()
        self.current_turn = -1 * self.current_turn
        return copy.deepcopy(self.board),reward,done

#==============COMING SOON=============