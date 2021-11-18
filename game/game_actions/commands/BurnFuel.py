from game.game_actions.interfaces.Command import Command
from game.game_actions.adapters import BurnFuelAdapter


class BurnFuel(Command):
    def __init__(self, burn_fuel_adt: BurnFuelAdapter):
        self.burn_fuel_adt = burn_fuel_adt
    
    def execute(self):
        new_pos = self.burn_fuel_adt.get_fuel_lvl() - self.burn_fuel_adt.get_fuel_velocity()
        self.burn_fuel_adt.burn_fuel(new_pos)
