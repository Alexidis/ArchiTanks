from game.game_actions.interfaces import FuelCheckable
from game.game_objects.UObject import UObject


class CheckFuelAdapter(FuelCheckable):
    def __init__(self, obj: UObject):
        self.obj = obj
    
    def get_fuel(self):
        return self.obj.get_property("fuel")
    
    def get_fuel_velocity(self):
        return self.obj.get_property("fuel_velocity")
