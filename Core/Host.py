from abc import ABC, abstractmethod


class Host(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self): pass
