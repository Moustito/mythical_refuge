from refuge.models.species import Dragon, Phoenix, Unicorn


def end_of_day_report(residents: list) -> None:
    for resident in residents:
        print(f"--- {resident.name} ---")
        print(resident.special_ability())
        print(f"Mission duration if sent: {resident.mission_duration_days()} days")
        print(resident)


class StatueDragon(Dragon):
    """A stone dragon displayed at the refuge entrance."""

    def special_ability(self) -> str:
        raise NotImplementedError("Statues have no abilities.")

    def refusal_reason(self) -> str | None:
        return "A statue cannot move."


class RoboticGuard:
    def __init__(self, name: str, model: str) -> None:
        self.name = name
        self.model = model

    def special_ability(self) -> str:
        return f"{self.name} patrols the perimeter and fires laser beams."

    def mission_duration_days(self) -> int:
        return 1

    def __str__(self) -> str:
        return f"{self.name} [Robotic Guard — model {self.model}]"


if __name__ == "__main__":
    frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")
    ember = Phoenix("Ember", "Ashlands", 72)
    pebble = Unicorn("Pebble", "Misty Hills", 25)

    print("=== 1. Three species, no type check ===")
    end_of_day_report([frostbite, ember, pebble])

    print("\n=== 2. With the statue (LSP violation) ===")
    statue = StatueDragon("Granite", "Refuge Entrance", 50, "stone")
    try:
        end_of_day_report([frostbite, statue, ember, pebble])
    except NotImplementedError as error:
        print(f"CRASH: {error}")

    print("\n=== 5. Duck typing: RoboticGuard, no parent ===")
    end_of_day_report([frostbite, ember, pebble, RoboticGuard("Sentinel", "RX-7")])