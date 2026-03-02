"""
Stub de simulation — Capteur ultrason avec réponse non-linéaire.

NE PAS MODIFIER CE FICHIER.
Traitez-le comme une boîte noire : vous savez ce qu'il expose (read()), pas comment il le calcule.
"""

import math


class FakeNonlinearUltrasoundSensor:
    """Simule un capteur ultrason dont la réponse est non-linéaire.

    La valeur brute retournée ne correspond pas à la distance réelle via une simple
    relation proportionnelle. Le capteur compresse les grandes distances et étire
    les petites — comme un vrai capteur ultrason bon marché.

    Tous les paramètres du constructeur ont des valeurs par défaut, mais vous pouvez
    les ajuster pour simuler différentes conditions.

    Paramètres
    ----------
    true_distance : float
        Distance réelle simulée (cm).
    """

    def __init__(
        self,
        true_distance: float = 80.0,
    ):
        self._true_distance: float = true_distance

    def _distort(self, distance: float) -> float:
        """Applique la distorsion non-linéaire interne (logarithmique)."""
        # Simule une courbe de réponse exponentielle.
        # La valeur brute est exprimée en unités arbitraires (pas des cm).
        return 200.0 * math.exp((distance / 200.0) - 1)

    def read(self) -> float:
        """Retourne la prochaine mesure brute."""
        return self._distort(self._true_distance)
