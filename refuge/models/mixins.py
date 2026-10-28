class FlyingMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flight_log: list[str] = []

    @staticmethod
    def travel_mode() -> str:
        return "by air"
    
    def fly(self, destination: str) -> str:
        message = f"{self.name} soars toward {destination}."
        self.flight_log.append(message)
        return message