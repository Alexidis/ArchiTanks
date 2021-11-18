class CommandException(Exception):
    def __init__(self):
        self.message = 'Команда не выполнена'
