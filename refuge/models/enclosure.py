from refuge.exceptions import ValidationError, EnclosureFullError, IncompatibleSpeciesError

class Enclosure():
    INCOMPATIBLE_PAIRS = frozenset({"Dragon", "Unicorn"}, {"Basilisk", "Phoenix"}, {"Basilisk", "Unicorn"})
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValidationError(f"Enter a capacity greater than 0. Got: {capacity}.")
        
        self.name = name
        self.capacity = capacity
        self._creatures: list = []

    @property
    def free_slots(self) -> int:
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

    def _Validate_creature(self, creature) -> None:
        '''Private helper that checks all constraints and raises specific errors if invalid.'''
        if any(c.name == creature.name for c in self._creatures):
                    raise ValidationError(f"{creature.name} is already in {self.name}.")
                
        if Enclosure.is_full(self):
            raise EnclosureFullError(f"{self.name} is full ({len(self._creatures)}/{self.capacity}).")
        
        for existing_creature in self._creatures:
            pair = frozenset({existing_creature.species, creature.species})
            if pair in self.INCOMPATIBLE_PAIRS:
                raise IncompatibleSpeciesError(f"A {creature.species} cannot live with a {existing_creature.species} in {self.name}.")

    def add(self, creature):
        '''Add a creature to the enclosure after validating constraints.'''
        self._Validate_creature(creature)

        self._creatures.append(creature)

    def can_accept(self, creature) -> bool:
        """Check if the enclosure can accept the creature without raising exceptions."""
        try:
            self._validate_creature(creature)
            return True
        except (ValidationError, EnclosureFullError, IncompatibleSpeciesError):
            return False