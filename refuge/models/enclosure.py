from refuge.exceptions import ValidationError

class Enclosure():
    INCOMPATIBLE_PAIRS = frozenset({"Dragon", "Unicorn"}, {"Basilisk", "Phoenix"}, {"Basilisk", "Unicorn"})
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValidationError(f"Enter a capacity greater than 0. Got: {capacity}.")
        
        self.name = name
        self.capacity = capacity
        self._creatures: list = []
