# playground.py
from refuge.exceptions import MissionRefusedError
from refuge.models.creature import Creature
from refuge.models.mixins import FlyingMixin


def send_to_field(creature: Creature) -> None:
    print(creature.special_ability())
    try:
        creature.send_on_mission()
    except MissionRefusedError as error:
        print(f"  ❌ refused: {error}")
    else:
        print(f"  → away for {creature.mission_duration_days()} days")

class WrongOrderDragon(FlyingMixin, Creature):
    def __init__(self, name, origin, power_level, element, **kwargs):
        super().__init__(name, "Dragon", origin, power_level, **kwargs)
        self.element = element

    def mission_duration_days(self) -> int:
        return 14
    
    def special_ability(self) -> str:
        return f"{self.name} breathes {self.element} and flies at great speed."
    
    def __repr__(self):
        return f"Dragon({super().__repr__()}, element={self.element!r})"