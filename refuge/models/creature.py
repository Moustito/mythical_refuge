class Creature:
    _total_creatures = 0
    VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")

    def __init__(self, name, species, origin, power_level):
        if not Creature.is_valid_species(species):
            raise ValueError(f"Unknown species: {species!r}.")

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
        return f"{self.name} {self.species} (origin: {self.origin}) [in refuge]" if self._in_refuge else f"{self.name} {self.species} (origin: {self.origin}) [on mission]"

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Creature.VALID_SPECIES

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["species"], data["origin"], data["power_level"])
    
    @classmethod
    def from_string(cls, text: str):
        champs = text.split(",")
        if len(champs) != 4:
            raise ValueError(f"The text must contain exactly 4 fields separated by commas. (received: {len(champs)})")
        name, species, origin, power_level = [c.strip() for c in champs]   
        return cls(name, species, origin, int(power_level))
    
    @classmethod
    def get_total_creatures(cls):
        return cls._total_creatures
