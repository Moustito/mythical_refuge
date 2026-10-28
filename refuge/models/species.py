from refuge.models.creature import Creature
from refuge.models.mixins import FlyingMixin

class Dragon(FlyingMixin, Creature):
    def __init__(self, name, origin, power_level, element, **kwargs):
        super().__init__(name, "Dragon", origin, power_level, **kwargs)
        self.element = element

    def mission_duration_days(self) -> int:
        return 14
    
    def special_ability(self) -> str:
        return f"{self.name} breathes {self.element} and flies at great speed."

    def __str__(self):
        return f"{super().__str__()} - element: {self.element}"
    
    def __repr__(self):
        return f"Dragon({super().__repr__()}, element={self.element!r})"

class Phoenix(FlyingMixin, Creature):
    def __init__(self, name, origin, power_level,**kwargs):
        super().__init__(name, "Phoenix", origin, power_level, **kwargs)
        self._resurrect = 0

    def resurrect(self):
        self._resurect =+ 1
        return f"🔥 {self.name} rises from its ashes! (resurrections: {self._resurect})"
    
    def mission_duration_days(self) -> int:
        return 7
    
    def special_ability(self) -> str:
        return f"{self.name} radiates a flame aura and rises again from its ashes."

class Unicorn(Creature):
    MIN_MISSION_POWER = 40

    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Unicorn", origin, power_level, **kwargs)
        
    def mission_duration_days(self) -> int:
        return 3
    
    def special_ability(self) -> str:
        return f"{self.name} heals its allies and gallops faster than the wind."
    
    def refusal_reason(self):
        if self.power_level < Unicorn.MIN_MISSION_POWER:
            return f"{self.name} is too weak for a mission (power {self.power_level} < 40)."
        return None
            

class Griffin(FlyingMixin, Creature):
    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Griffin", origin, power_level, **kwargs)
        
    def mission_duration_days(self) -> int:
        return 10
    
    def special_ability(self) -> str:
        return f"{self.name} dives from the clouds with razor-sharp talons."

class Basilisk(Creature):
    def __init__(self, name, origin, power_level, **kwargs):
        super().__init__(name, "Basilisk", origin, power_level, **kwargs)
        
    def mission_duration_days(self) -> int:
        return 5
    
    def special_ability(self) -> str:
        return f"{self.name} petrifies its enemies with a single gaze."

