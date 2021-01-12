from dataclasses import dataclass, field
from animals import Animal


@dataclass
class Zoo:
    animals: list[Animal] = field(default_factory=list)
