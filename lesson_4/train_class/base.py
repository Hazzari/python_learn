from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Vehicle(ABC):
    _model: str
    _long: int = None
    _carrying_capacity: int = 0
    _max_speed: int = 0
    _weight: int = field(default_factory=int)
    _speed: int = field(repr=False, default=0)
    _sound: str = field(repr=False, default=None)

    def __post_init__(self):
        self._model = self.model

    @property
    def model(self):
        return self._model

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError

    @abstractmethod
    def speed_up(self):
        raise NotImplementedError

    @abstractmethod
    def speed_down(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError
    #
    # def __str__(self):
    #     return self.title
    #
    # def __repr__(self):
    #     return self.__str__()
