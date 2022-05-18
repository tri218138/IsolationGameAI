from interface_game.Minmax_class import *
from Minimax_Isolation import *
import random

class MinimaxII(MinimaxInterface):
    def __init__(self,depth,path = {}):
        self.env = MinimaxIsolation(depth,None)
        self.path = path
        self.depth = depth
        self.board = self.env.board
        
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
    
    def minimax_act(self,board,player):
        if self.depth == 0:
            return self.sample_act(board,player)
        # print("Board-pre: ",board)
        old,new = self.env.aimove(board,player) 
        board = self.env.board.copy()
        # print("Board-after: ",board)
        return old,new
    
    def check_win(self,board,player):
        return self.env.evaluate_board(board,player),self.env.checkEnd(board,player)
    
    def player_act(self,board,player):
        self.env.player_move(board,player)
        board = self.env.board
        # self.board = self.env.board
    
    def getBoard(self):
        return self.board