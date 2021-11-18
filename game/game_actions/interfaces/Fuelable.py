from abc import ABC, abstractmethod


class Fuelable(ABC):

    @abstractmethod
    def get_fuel_lvl(self):
        pass

    @abstractmethod
    def burn_fuel(self, new_value):
        pass

    @abstractmethod
    def get_fuel_velocity(self):
        pass
 