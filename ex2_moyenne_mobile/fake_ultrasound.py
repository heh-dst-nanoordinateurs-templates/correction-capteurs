"""
Stub de simulation — Capteur ultrason bruité.

NE PAS MODIFIER CE FICHIER.
Traitez-le comme une boîte noire : vous savez ce qu'il expose (read()), pas comment il le calcule.
"""

import random


class FakeUltrasoundSensor:
    """Simule un capteur ultrason affecté de bruit gaussien.

    Chaque appel à read() retourne la distance réelle à laquelle s'ajoute
    un bruit aléatoire centré en zéro. Les valeurs peuvent légèrement dépasser
    la plage physique du capteur à cause du bruit.

    Tous les paramètres du constructeur ont des valeurs par défaut, mais vous pouvez
    les ajuster pour simuler différentes conditions.

    Paramètres
    ----------
    true_distance : float
        Distance réelle simulée (cm).
    noise_std : float
        Écart-type du bruit gaussien (cm).
    """

    def __init__(
        self,
        true_distance: float = 50.0,
        noise_std: float = 8.0,
    ):
        self._true_distance: float = true_distance
        self._noise_std: float = noise_std

    def read(self) -> float:
        """Retourne la prochaine mesure brute (distance réelle + bruit)."""
        return self._true_distance + random.gauss(0, self._noise_std)
