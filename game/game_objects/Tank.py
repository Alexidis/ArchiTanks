from .UObject import UObject


class Tank(UObject):
    
    def __init__(self, position=None, direction=0):
        self.position = position or [0, 0]
        self.velocity = [0, 0]
        self.direction = direction
        self.angle_velocity = 0
        
    def get_property(self, prop_name: str):
        return self.__dict__[prop_name]
    
    def set_property(self, prop_name: str, new_value):
        self.__dict__[prop_name] = new_value
