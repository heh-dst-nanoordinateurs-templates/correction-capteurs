"""
Stub de simulation — Capteur ultrason avec valeurs aberrantes.

NE PAS MODIFIER CE FICHIER.
Traitez-le comme une boîte noire : vous savez ce qu'il expose (read()), pas comment il le calcule.
"""

import random


class FakeUltrasoundSensor:
    """Simule un capteur ultrason qui produit parfois des valeurs hors limites.

    La plupart du temps, read() retourne une valeur dans la plage physique du capteur.
    Avec une probabilité outlier_prob, il retourne une valeur aberrante typique
    (0 cm ou 400 cm) correspondant aux pannes courantes de ce type de capteur.

    Tous les paramètres du constructeur ont des valeurs par défaut, mais vous pouvez
    les ajuster pour simuler différentes conditions.

    Paramètres
    ----------
    true_distance : float
        Distance réelle simulée (cm).
    min_valid : float
        Borne inférieure de la plage de mesure valide (cm).
    max_valid : float
        Borne supérieure de la plage de mesure valide (cm).
    outlier_prob : float
        Probabilité (entre 0 et 1) qu'une lecture soit aberrante.
    """

    def __init__(
        self,
        true_distance: float = 50.0,
        min_valid: float = 2.0,
        max_valid: float = 400.0,
        outlier_prob: float = 0.2,
    ):
        self._true_distance: float = true_distance
        self._min_valid: float = min_valid
        self._max_valid: float = max_valid
        self._outlier_prob: float = outlier_prob
        self._range: float = max_valid - min_valid

    def read(self) -> float:
        """Retourne la prochaine mesure brute (valide ou aberrante)."""
        if random.random() < self._outlier_prob:
            return random.choice([self._min_valid - self._range * 0.1, self._max_valid + self._range * 0.1])
        return self._true_distance + random.gauss(0, 1.0)
