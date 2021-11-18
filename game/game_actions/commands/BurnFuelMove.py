from .MacroCommand import MacroCommand


class BurnFuelMove(MacroCommand):
    def execute(self):
        for command in self.commands:
            command.execute()
    