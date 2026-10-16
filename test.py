from refuge.models.creature import Creature

row = {"id": 1, "name": "Frostbite", "species": "Dragon", "origin": "Nordic Realms", "power_level": 95}
frostbite = Creature.from_dict(row)
ember = Creature.from_string("Ember, Phoenix, Ashlands, 72")

print(frostbite)
frostbite.send_on_mission()
print(frostbite)
