"""
Stub de simulation — Capteur de température avec offset.

NE PAS MODIFIER CE FICHIER.
Traitez-le comme une boîte noire : vous savez ce qu'il expose (read()), pas comment il le calcule.
"""

import random


class FakeTemperatureSensor:
    """Simule un capteur de température affecté d'un offset systématique.

    Chaque appel à read() retourne une valeur aléatoire à laquelle s'ajoute toujours le même offset constant.

    Tous les paramètres du constructeurs ont des valeurs par défaut, mais vous pouvez les ajuster pour simuler
    différentes conditions.

    Paramètres
    ----------
    min_temp : float
        Borne inférieure de la plage de températures réelles simulées (°C).
    max_temp : float
        Borne supérieure de la plage de températures réelles simulées (°C).
    offset : float
        Décalage constant injecté dans toutes les lectures (°C).
    """

    def __init__(
        self,
        min_temp: float = 16.0,
        max_temp: float = 35.0,
        offset: float = 4.2,
    ):
        self._min_temp: float = min_temp
        self._max_temp: float = max_temp
        self._offset: float = offset

    def read(self) -> float:
        """Retourne la prochaine mesure brute."""
        return random.uniform(self._min_temp, self._max_temp) + self._offset
