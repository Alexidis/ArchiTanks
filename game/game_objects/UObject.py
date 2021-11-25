from abc import ABC, abstractmethod


class UObject(ABC):
    __is_frozen = False
    
    def __setattr__(self, key, value):
        if self.__is_frozen and not hasattr(self, key):
            raise AttributeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)
    
    def _freeze(self):
        self.__is_frozen = True

    @abstractmethod
    def get_property(self, prop_name: str):
        pass

    @abstractmethod
    def set_property(self, prop_name: str, new_value):
        pass
