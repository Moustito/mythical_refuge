class Creature:
    _total_creatures = 0

    def __init__(self, name, species, origin, power_level):
        self.name = name
        self.species = species
        self.origin = origin
        self.power_level = power_level
        self.in_refuge = True

        Creature._total_creatures += 1

    def send_on_mission(self):
        self.in_refuge = False
    
    def return_to_refuge(self):
        self.in_refuge = True