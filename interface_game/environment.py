from time import time
import random
from abc import ABCMeta, abstractmethod

class BaseEnvironment:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self,depth,path={}):
        pass

    @abstractmethod
    def env_act(self):
        pass
     
    @abstractmethod
    def reset(self,player,depth,path):
        pass
    
    @abstractmethod
    def check_win(self):
        pass
    
    @abstractmethod
    def step(self,action):
        pass