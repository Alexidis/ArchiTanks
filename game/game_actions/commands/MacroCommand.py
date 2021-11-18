from game.game_actions.interfaces.Command import Command
from abc import ABC, abstractmethod
from typing import List
command_list = List[Command]


class MacroCommand(ABC):
    def __init__(self, commands: command_list):
        self.commands = commands
    
    @abstractmethod
    def execute(self):
        pass
