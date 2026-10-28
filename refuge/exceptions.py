class RefugeError(Exception):
    """Base de toutes les erreurs métier du refuge."""


class ValidationError(RefugeError):
    """Levée lorsqu'une donnée métier est invalide (espèce inconnue, puissance incorrecte, etc.)."""

class MissionRefusedError(RefugeError):
    """ """