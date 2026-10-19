# playground.py
from refuge.exceptions import MissionRefusedError
from refuge.models.creature import Creature


def send_to_field(creature: Creature) -> None:
    print(creature.special_ability())
    try:
        creature.send_on_mission()
    except MissionRefusedError as error:
        print(f"  ❌ refused: {error}")
    else:
        print(f"  → away for {creature.mission_duration_days()} days")