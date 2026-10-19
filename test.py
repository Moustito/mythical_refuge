from refuge.models.creature import Creature
from refuge.models.species import Dragon, Phoenix, Unicorn, Griffin
from refuge.models.mixins import FlyingMixin
from playground.playground  import send_to_field

frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")
print([cls.__name__ for cls in Dragon.__mro__])
print(frostbite.travel_mode())
print(frostbite.fly("Frozen Peaks"))
print(frostbite.flight_log)
print(Unicorn("Moonbeam", "Crystal Lake", 67).travel_mode())
