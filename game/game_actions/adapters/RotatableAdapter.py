from game.game_actions.interfaces import Rotatable
from game.game_objects.UObject import UObject


class RotatableAdapter(Rotatable):
    def __init__(self, obj: UObject):
        self.obj = obj

    def get_direction(self):
        return self.obj.get_property("direction")

    def set_direction(self, new_value):
        self.obj.set_property("direction", new_value)

    def get_angle_velocity(self):
        return self.obj.get_property("angle_velocity")
