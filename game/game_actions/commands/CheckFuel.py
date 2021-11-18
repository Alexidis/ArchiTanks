from game.game_actions.interfaces.Command import Command
from game.game_actions.adapters import CheckFuelAdapter
from game.Exceptions import CommandException


class CheckFuel(Command):
    def __init__(self, chk_fuel_adt: CheckFuelAdapter):
        self.chk_fuel_adt = chk_fuel_adt
    
    def execute(self):
        new_fuel_level = self.chk_fuel_adt.get_fuel() - self.chk_fuel_adt.get_fuel_velocity()
        if new_fuel_level < 0:
            raise CommandException

