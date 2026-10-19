from refuge.exceptions import ValidationError, MissionRefusedError
from abc import ABC, abstractmethod

class Creature(ABC):
    # 1. Docstring
    # 2. Class Atributes
    _total_creatures = 0
    VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")

    # 3. __init__ instance attributes
    def __init__(self, name, species, origin, power_level, **kwargs):
        if not Creature.is_valid_species(species):
            raise ValidationError(f"Unknown species: {species!r}.")

        self.name = name
        self.species = species
        self.__origin = origin
        self.power_level = power_level
        self._in_refuge = True

        Creature._total_creatures += 1

        super().__init__(**kwargs)

    # 4. Alternate constructors
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
    
    # 5. Properties and setters
    @property
    def power_level(self):
        return self._power_level
    
    @power_level.setter
    def power_level(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError(f"power_level must be an int, got {type(value).__name__}.")
        if not 0 <= value <= 100:
            raise ValidationError(f"power_level must be between 0 and 100, got {value}.")
        self._power_level = value
    
    @property
    def in_refuge(self):
        return self._in_refuge

    @property
    def origin(self):
        return self.__origin

    @abstractmethod
    def mission_duration_days() -> int:
        """Send in day the mission duration"""

    @abstractmethod
    def special_ability() -> str:
        """Send the name of special ability"""

    # 6. public methods - instance methods
    def send_on_mission(self):
        """
        Send a creature on mission.
        Raises MissionRefusedError when the creature cannot leave.
        """
        if not self._in_refuge:
            raise MissionRefusedError(f"{self.name} is already on a mission.")
        
        reason = self.refusal_reason()
        if reason is not None:
            raise MissionRefusedError(reason)
        
        self._in_refuge = False

    def refusal_reason(self) -> str | None:
        """
        Hook : send a refuse message, or None if the creature can leave.

        By default, no reason to refuse. The sub-classes can redifine.
        """
        return None
    
    def return_to_refuge(self):
        self._in_refuge = True

    # 7. Dunder methods
    def __str__(self):
        return f"{self.name} {self.species} (origin: {self.origin}) [{"in refuge" if self._in_refuge else "on mission"}]"
    
    def __repr__(self):
        return f"Creature(name={self.name!r}, species={self.species!r}, origin={self.origin!r}, power_level={self.power_level!r})"

    # 8. Static methods
    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in Creature.VALID_SPECIES
    
    @staticmethod
    def travel_mode() -> str:
        return "on foot"

    # 9. private methods - instance methods









    
    

