from abc import ABCMeta, abstractmethod

class BaseAgent:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    
    @abstractmethod
    def agent_init(self, agent_info):
        pass
    
    @abstractmethod
    def agent_start(self, observation):
        pass 
        
    @abstractmethod
    def agent_step(self, reward, observation):
        pass

    @abstractmethod
    def agent_end(self, reward):
        pass

    @abstractmethod
    def agent_cleanup(self):
        pass 
        
    @abstractmethod
    def agent_message(self, message):
        pass