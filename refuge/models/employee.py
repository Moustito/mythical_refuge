from abc import ABC, abstractmethod
from refuge.exceptions import ValidationError

class Employee(ABC):
    ROLE = "employee"
    PERMISSIONS: frozenset[str] = frozenset()

    def __init__(self, full_name: str, email: str):
        if "@" not in email:
            raise ValidationError(f"There is no '@' in your email. email: {email}.")
        
        self.full_name = full_name
        self.email = email
    
    def can(self, permission: str) -> bool:
        return permission in self.PERMISSIONS
    
    def can_escort(self, creature) -> bool:
        """by default, an employee does not escort"""
        return False

    @abstractmethod
    def describe_duties(self) -> str:
        """Describe duties of the employee"""

    def __str__(self):
        return f"{self.full_name} ({self.ROLE})"
    
class Handler(Employee):
    ROLE = "handler"
    PERMISSIONS = frozenset({"escort_mission"})

    def __init__(self, full_name: str, email: str, certification_level: int) -> None:
        super().__init__(full_name, email)
        self.certification_level = certification_level

    @property
    def certification_level(self) -> int:
        return self._certification_level
    
    @certification_level.setter
    def certification_level(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError(f"certification_level must be an int, got {type(value).__name__}.")
        if not 1 <= value <= 5:
            raise ValidationError(f"certification_level must be between 1 and 5, got {value}.")
        self._certification_level = value
    
    def can_escort(self, creature) -> bool:
        """
        by default, an employee does not escort, but the handler can escort 
        if certification is bigger than the power level's creature.
        """
        return self.certification_level * 20 >= creature.power_level
    
    def describe_duties(self) -> str:
        max_power = self.certification_level * 20
        return f"{self.full_name} escorts creatures up to power {max_power}."

    def __str__(self):
        base = super().__str__()
        return f"{base.removesuffix(')')}, level {self.certification_level})"

class Veterinarian(Employee):
    ROLE = "veterinarian" 
    PERMISSIONS = frozenset({"perform_checkup"})

    def __init__(self, full_name: str, email: str) -> None:
        super().__init__(full_name, email)
    
    def describe_duties(self) -> str:
        return f"{self.full_name} examines and treats the creatures."
    
    def perform_checkup(self, creature, status: str, diagnosis: str) -> str:
        return f"{self.full_name} examined {creature}: {status} ({diagnosis})."