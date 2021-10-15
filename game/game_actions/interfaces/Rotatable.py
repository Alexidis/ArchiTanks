from abc import ABC, abstractmethod


class Rotatable(ABC):
    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def set_direction(self, new_value):
        pass

    @abstractmethod
    def get_angle_velocity(self):
        pass
