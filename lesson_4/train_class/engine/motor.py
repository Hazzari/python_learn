from dataclasses import dataclass, field


@dataclass(frozen=True)
class Motor:
    title: str
    engine_volume: int
    capacity: int
    fuel_consumption: int
    number_of_cylinders: int = field(default_factory=int)
