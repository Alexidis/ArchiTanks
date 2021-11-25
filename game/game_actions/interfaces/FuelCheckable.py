from abc import ABC, abstractmethod


class FuelCheckable(ABC):
    
    @abstractmethod
    def get_fuel(self):
        pass
    
    @abstractmethod
    def get_fuel_velocity(self):
        pass
