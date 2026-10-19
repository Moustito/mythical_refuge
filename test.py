from refuge.models.creature import Creature
from refuge.models.species import Dragon, Phoenix, Unicorn, Griffin
from refuge.models.mixins import FlyingMixin
from playground.playground  import send_to_field

def end_of_day_report(residents: list) -> None:
    for resident in residents:
        print(f"--- {resident.name} ---")
        print(resident.special_ability())
        print(f"Mission duration if sent: {resident.mission_duration_days()} days")
        print(resident)

end_of_day_report([Dragon("Frostbite", "Nordic Realms", 95, "ice"), Phoenix("Blaze", "Volcanic Isles", 88), Unicorn("Moonbeam", "Crystal Lake", 67), Griffin("Skyclaw", "Mountain Heights", 80)])
