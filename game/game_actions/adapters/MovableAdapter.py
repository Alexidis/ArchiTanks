from game.game_actions.interfaces import Movable
from game.game_objects.UObject import UObject
from typing import List
position = List[float]


class MovableAdapter(Movable):
    def __init__(self, obj: UObject):
        self.obj = obj
        
    def get_position(self) -> position:
        return self.obj.get_property("position")
    
    def set_position(self, new_value: position):
        self.obj.set_property("position", new_value)
    
    def get_velocity(self):
        return self.obj.get_property("velocity")
