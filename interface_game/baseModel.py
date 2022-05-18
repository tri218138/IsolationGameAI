from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def __init__(self, info = {}):
        pass

    @abstractmethod
    def observe(self, state, action_space: list = None):
        pass

    @abstractmethod
    def observe_on_training(self, state, action_space: list = None) -> int:
        pass

    @abstractmethod
    def take_reward(self, reward, next_state, done):
        pass

    @abstractmethod
    def train_network(self, sample_size: int, batch_size: int, epochs: int, verbose: int = 2, cer_mode: bool = False):
        pass

    @abstractmethod
    def update_target_network(self):
        pass