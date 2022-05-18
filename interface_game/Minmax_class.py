from time import time
import numpy as np
import random
from abc import ABCMeta, abstractmethod
from parameter import *
import copy

#append docstring for function implementation
class Minimax(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self,depth,board = None):
        pass
    
    @abstractmethod
    def get_all_nearby_cell(self,x,y):
        pass        
        
    @abstractmethod
    def get_all_empty_cell(self,board,x,y):
        pass
        
    @abstractmethod
    def move(self,board,player): 
        pass
    
    @abstractmethod
    def aimove(self,board,player):
        pass
    
    @abstractmethod
    def print_board(self,board):
        pass
    
    @abstractmethod
    def evaluate_board(self,board,agent_flag):
        pass
    
    @abstractmethod
    def in_board(self,x,y):
        pass
        
    @abstractmethod
    def checkEnd(self,board,agent_flag):
        pass
            
    @abstractmethod
    def clone_board(self,board):
        pass
            
    @abstractmethod
    def minimax(self,board,player,maximizer,alpha,beta,depth):
        pass
        
    @abstractmethod
    def get_player_piece(self,board,agent_flag):
        pass
    
    @abstractmethod
    def strategy1_check_point(self,board,componet_flag,cell):
        pass
        
    @abstractmethod
    def strategy1_block_move(self,board,component_flag,component_cell):
        pass
                    
    @abstractmethod
    def player_move(self,board,player):
        pass
        
        
    @abstractmethod
    def move_piece(self,board,player_flag,old_cell,new_cell):
        pass
        
    # @abstractmethod
    # def strategy2_block_move(self,component_flag,compoent_cell):
    #     pass

class MinimaxInterface(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self,depth,path = {}):
        pass
    
    @abstractmethod
    def get_act_space(self,board,player):
        pass
    
    @abstractmethod
    def sample_act(self,board,player):
        pass
    
    @abstractmethod
    def minimax_act(self,board,player):
        pass
    
    @abstractmethod
    def getBoard(self):
        pass