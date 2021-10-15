from abc import ABC, abstractmethod


class Movable(ABC):

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def set_position(self, new_value):
        pass

    @abstractmethod
    def get_velocity(self):
        pass
