from game.game_actions.interfaces.Command import Command
from ..adapters import MovableAdapter


class Move(Command):
    def __init__(self, movable_adt: MovableAdapter):
        self.movable_adt = movable_adt

    def execute(self):
        
        new_pos = [x + y for x, y in zip(self.movable_adt.get_position(), self.movable_adt.get_velocity())]
        self.movable_adt.set_position(new_pos)
