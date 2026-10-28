from refuge.exceptions import ValidationError

class Enclosure():
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValidationError(f"Enter a capacity greater than 0. Got: {capacity}.")
        
        self.name = name
        self.capacity = capacity
        self._creatures: list = []