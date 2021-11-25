from game.game_actions.interfaces import Fuelable
from game.game_objects.UObject import UObject


class BurnFuelAdapter(Fuelable):
    def __init__(self, obj: UObject):
        self.obj = obj
    
    def get_fuel_lvl(self) -> float:
        return self.obj.get_property("fuel")
    
    def burn_fuel(self, new_value: float):
        self.obj.set_property("fuel", new_value)
    
    def get_fuel_velocity(self) -> float:
        return self.obj.get_property("fuel_velocity")
