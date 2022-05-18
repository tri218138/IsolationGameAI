import os
import pygame
from pygame.transform import scale
import time
from parameter import *
import numpy as np

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(200, 35)

class Gui(object):
    def __init__(self,board, valid = POS['VALID'], auto = False):
        self.board = board
        self.dim = len(board)
        self.valid = valid
        self.auto = auto
        pygame.init()
        self.window = pygame.display.set_mode((1100,800))
        self.game_font = pygame.font.Font('FileGame/04B_19.TTF',40)
        self.window.fill(BLACK)
        
    def draw_board(self):
        for r in range(0, SHAPE[1]):
            for c in range(0, SHAPE[0]):
                rect = pygame.Rect(c * EDGE + MARGIN + OFFSET, r * EDGE + MARGIN + OFFSET, EDGE - 2*MARGIN, EDGE - 2*MARGIN)
                if self.board[r][c] != BLOCK:                 
                    pygame.draw.rect(self.window, YELLOW, rect)
                elif self.board[r][c] == BLOCK:
                    pygame.draw.rect(self.window, BLACK, rect)
                
        for i in range(len(self.valid)):
            rect = pygame.Rect(self.valid[i][1] * EDGE + MARGIN + OFFSET, self.valid[i][0] * EDGE + MARGIN + OFFSET, EDGE - 2*MARGIN, EDGE - 2*MARGIN)      
            pygame.draw.rect(self.window, GREEN, rect)  
        pygame.draw.circle(self.window, RED, (POS['ACTIVE_P1'][1] * EDGE + int(EDGE / 2) + OFFSET, POS['ACTIVE_P1'][0] * EDGE + int(EDGE / 2) + OFFSET), int(EDGE / 2 - 2*MARGIN)) 
        pygame.draw.circle(self.window, BLUE, (POS['ACTIVE_P2'][1] * EDGE + int(EDGE / 2) + OFFSET, POS['ACTIVE_P2'][0] * EDGE + int(EDGE / 2) + OFFSET), int(EDGE / 2 - 2*MARGIN))  
        # print(POS['SELECT'])
        
        
    def render_font(self,turn = 0,time = 0):
        intro_surface = self.game_font.render(f'ISOLATION',True,red)
        intro_rect = intro_surface.get_rect(center = (925,300))
        self.window.blit(intro_surface,intro_rect)
        
        # score_surface = self.game_font.render(f'LEVEL: {self.dim}x{self.dim}',True,WHITE)
        # score_rect = score_surface.get_rect(center = (925,450))
        # self.window.blit(score_surface,score_rect)
        if self.auto == True and not ENDGAME[0]:
            return
        if not ENDGAME[0]:
            global TURN
            value = ' '
            if TURN[0] == 0:        
                value = 'PLAYER 1 MOVE'
            elif TURN[0] == 1:        
                value = 'PLAYER 1 BLOCK'
            elif TURN[0] == 2:        
                value = 'PLAYER 2 MOVE'
            elif TURN[0] == 3:        
                value = 'PLAYER 2 BLOCK'
            high_score_surface = self.game_font.render(value,True,WHITE)
            high_score_rect = high_score_surface.get_rect(center = (925,520))
            self.window.blit(high_score_surface,high_score_rect)
        else:
            value = ' '
            if TURN[0] == 0:
                value = 'PLAYER 2 WIN!'
            elif TURN[0] == 2:
                value = 'PLAYER 1 WIN!'
            else:
                value = 'TIE'
            result_surface = self.game_font.render(value,True,WHITE)  
            result_rect = result_surface.get_rect(center = (925,590))
            self.window.blit(result_surface,result_rect)
    
    def display(self, step = 0,time_ = 0, second = 1):
        # pygame.init()
        self.render_font(step,time_)
        self.draw_board()
        pygame.display.flip()  # Refresh display
        # time.sleep(second / 2)
