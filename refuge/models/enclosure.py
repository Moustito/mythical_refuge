from refuge.exceptions import ValidationError

class Enclosure():
    INCOMPATIBLE_PAIRS = frozenset({"Dragon", "Unicorn"}, {"Basilisk", "Phoenix"}, {"Basilisk", "Unicorn"})
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValidationError(f"Enter a capacity greater than 0. Got: {capacity}.")
        
        self.name = name
        self.capacity = capacity
        self._creatures: list = []

    @property
    def free_slots(self) -> str:
        '''Calculate the number of free slots in an enclosure.'''
        return self.capacity - len(self._creatures)

    @property
    def is_full(self) -> bool:
        '''Check if the enclosure is full.'''
        return len(self._creatures) >= self.capacity

    @property
    def species(self) -> set[str]:
        '''Return all unique species present in the enclosure.'''
        return {creature.species for creature in self._creatures}