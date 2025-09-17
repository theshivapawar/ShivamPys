from abc import ABC, abstractmethod

class Desert(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_cost(self):
        pass