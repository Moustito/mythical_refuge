class Creature:
    _total_creatures = 0
    VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")

    def __init__(self, name, species, origin, power_level):
        self.name = name
        self.species = species
        self.origin = origin
        self.power_level = power_level
        self._in_refuge = True

        Creature._total_creatures += 1

    def send_on_mission(self):
        self._in_refuge = False
    
    def return_to_refuge(self):
        self._in_refuge = True

    def __str__(self):
        return ("Frostbite the Dragon (origin: Nordic Realms) [in refuge]" if self._in_refuge else "Frostbite the Dragon (origin: Nordic Realms) [on mission]")

    def is_valid_species(species: str):
        return (True if species in VALID_SPECIES else False)
