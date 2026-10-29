from dataclasses import dataclass, field
from decimal import Decimal
from datetime import date, timedelta
from refuge.exceptions import ValidationError


@dataclass(eq=False)
class Mission:
    creature_name: str
    handler_name: str
    destination: str
    departure_date: date
    duration_days: int
    base_reward: Decimal
    danger_multiplier: Decimal = Decimal("1.0")
    returned_on: date | None = None
    notes: str = ""
    id: int | None = field(default=None, repr=False)

    def __post_init__(self):
        if not self.destination.strip():
            raise ValidationError(f"Need destination")
        if not isinstance(self.duration_days, int) or isinstance(self.duration_days, bool) or self.duration_days <= 0:
            raise ValidationError(f"duration_days must be a positive integer, got {self.duration_days}.")
        
        self.base_reward = Decimal(str(self.base_reward))
        self.danger_multiplier = Decimal(str(self.danger_multiplier))

        if self.base_reward < 0:
            raise ValidationError("Base reward cannot be negative.")

    @property
    def due_date(self):
        '''Calcule la date de fin de la mission.
        due_date = departure_date + duration_days'''
        return self.departure_date + timedelta(days=self.duration_days)

    @property
    def reward(self):
        '''Calcule de la recompense mutiplier par le danger. 
        reward = base_reward * danger_multiplier'''
        return self.base_reward * self.danger_multiplier

    @property
    def is_completed(self):
        '''Renvoie si la mission est complété ou en cours'''
        pass

    def is_overdue(today: date | None = None) -> bool:
        pass

    def mark_returned(on: date):
        pass

    def days_late() -> int:
        pass