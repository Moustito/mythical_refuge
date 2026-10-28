class RefugeError(Exception):
    """Base de toutes les erreurs métier du refuge."""


class ValidationError(RefugeError):
    """Levée lorsqu'une donnée métier est invalide (espèce inconnue, puissance incorrecte, etc.)."""

class MissionRefusedError(RefugeError):
    """ """

class EnclosureFullError(RefugeError):
    '''Raise an error when the enclosure is full'''

class IncompatibleSpeciesError(RefugeError):
    '''Raise an error when a species incompatibility is detected in an enclosure.'''