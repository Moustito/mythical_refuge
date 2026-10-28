from refuge.exceptions import ValidationError, EnclosureFullError, IncompatibleSpeciesError
from refuge.models.creature import Creature

class Enclosure():
    INCOMPATIBLE_PAIRS = frozenset({
        frozenset({"Dragon", "Unicorn"}),
        frozenset({"Basilisk", "Phoenix"}),
        frozenset({"Basilisk", "Unicorn"})
    })
    
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValidationError(f"Enter a capacity greater than 0. Got: {capacity}.")
        
        self.name = name
        self.capacity = capacity
        self._creatures: list = []

    #Properties
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

    #Pricate helper
    def _validate_creature(self, creature) -> None:
        '''Private helper that checks all constraints and raises specific errors if invalid.'''
        if any(c.name == creature.name for c in self._creatures):
                    raise ValidationError(f"{creature.name} is already in {self.name}.")
                
        if self.is_full:
            raise EnclosureFullError(f"{self.name} is full ({len(self._creatures)}/{self.capacity}).")
        
        for existing_creature in self._creatures:
            pair = frozenset({existing_creature.species, creature.species})
            if pair in self.INCOMPATIBLE_PAIRS:
                raise IncompatibleSpeciesError(f"A {creature.species} cannot live with a {existing_creature.species} in {self.name}.")

    # public method
    def add(self, creature):
        '''Add a creature to the enclosure after validating constraints.'''
        self._validate_creature(creature)

        self._creatures.append(creature)

    def can_accept(self, creature) -> bool:
        """Check if the enclosure can accept the creature without raising exceptions."""
        try:
            self._validate_creature(creature)
            return True
        except (ValidationError, EnclosureFullError, IncompatibleSpeciesError):
            return False

    def remove(self, name: str) -> Creature:
        '''Remove and return a creature from the enclosure by its name.

        Args:
            name (str): The name of the creature to remove.

        Returns:
            Creature: The removed creature object.

        Raises:
            ValidationError: If no creature with this name is found in the enclosure.'''
        for creature in self._creatures:
             if creature.name == name:
                  self._creatures.remove(creature)
                  return creature
        raise ValidationError(f"{name} is not in {self.name}.")

    #Dunder method
    def __len__(self):
        return len(self._creatures)

    def __contains__(self, name):
        return any(c.name == name for c in self._creatures)

    def __iter__(self):
        for creature in self._creatures:
            yield creature
 
    def __getitem__(self, name: str):
        for creature in self._creatures:
            if creature.name == name:
                return creature
        raise KeyError(f"No creature named '{name}' found in {self.name}.")

    def __repr__(self):
        creature_name = [c.name for c in self._creatures]
        return f"Enclosure({self.name}, {len(self._creatures)}/{self.capacity}: {creature_name})"