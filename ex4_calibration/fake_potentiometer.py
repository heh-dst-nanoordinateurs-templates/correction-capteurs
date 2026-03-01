"""
Stub de simulation — Potentiomètre analogique non calibré.

NE PAS MODIFIER CE FICHIER.
Traitez-le comme une boîte noire : vous savez ce qu'il expose (read(), sweep()), pas comment il le calcule.
"""

import random


class FakePotentiometer:
    """Simule un potentiomètre lu via un convertisseur analogique-numérique (ADC).

    Les valeurs brutes ne correspondent pas à des pourcentages : elles dépendent
    des limites mécaniques et électriques réelles du potentiomètre, qui varient
    d'un composant à l'autre. Une calibration est nécessaire pour les interpréter.

    Tous les paramètres du constructeur ont des valeurs par défaut, mais vous pouvez
    les ajuster pour simuler différentes conditions.

    Paramètres
    ----------
    raw_min : float
        Valeur brute ADC quand le potentiomètre est à la butée gauche (0 %).
    raw_max : float
        Valeur brute ADC quand le potentiomètre est à la butée droite (100 %).
    noise_std : float
        Écart-type du bruit gaussien sur les lectures (du à l'ADC).
    """

    def __init__(
        self,
        raw_min: float = 312.0,
        raw_max: float = 29850.0,
        noise_std: float = 50.0,
    ):
        self._raw_min: float = raw_min
        self._raw_max: float = raw_max
        self._noise_std: float = noise_std
        self._position: float = 0.5  # position interne entre 0.0 et 1.0

    def _read_raw(self) -> float:
        """Retourne la lecture ADC brute à la position actuelle du potentiomètre, sans bruit."""
        return self._raw_min + self._position * (self._raw_max - self._raw_min)

    def read(self) -> float:
        """Retourne la lecture ADC à la position actuelle du potentiomètre + un peu de bruit."""
        raw = self._read_raw()
        return raw + random.gauss(0, self._noise_std)

    def set_position(self, position: float):
        """Positionne le potentiomètre à une valeur entre 0.0 (butée gauche) et 1.0 (butée droite)."""
        if not (0.0 <= position <= 1.0):
            raise ValueError("position doit être entre 0.0 et 1.0")
        self._position = position

    def sweep(self, steps: int = 20) -> list[float]:
        """Simule un balayage complet du potentiomètre (butée gauche → butée droite).

        Retourne une liste de `steps` lectures brutes correspondant à des positions
        régulièrement espacées de 0 % à 100 %.

        Paramètres
        ----------
        steps : int
            Nombre de positions échantillonnées lors du balayage.
        """
        readings = []
        self.set_position(0.0)  # commence à la butée gauche
        for i in range(steps):
            self.set_position(i / (steps - 1))
            readings.append(self._read_raw())
        self.set_position(0.5)  # remet au centre après le balayage
        return readings
