from game.game_actions.interfaces.Command import Command
from game.game_actions.adapters import RotatableAdapter


class Rotate(Command):
    def __init__(self, movable_adt: RotatableAdapter):
        self.movable_adt = movable_adt
    
    def execute(self):
        FULL_CIRCLE = 360
        new_direction = (self.movable_adt.get_direction() + self.movable_adt.get_angle_velocity()) % FULL_CIRCLE
        self.movable_adt.set_direction(new_direction)
