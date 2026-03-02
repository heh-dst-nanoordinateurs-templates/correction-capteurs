from fake_ultrasound_nonlinear import FakeNonlinearUltrasoundSensor

# Table de calibration fournie : (valeur_brute, distance_réelle_cm)
# Ces points ont été mesurés avec un instrument de référence.
CALIBRATION_TABLE: list[tuple[float, float]] = [
    (77.3, 10.0),
    (85.5, 30.0),
    (94.5, 50.0),
    (109.8, 80.0),
    (134.0, 120.0),
    (172.1, 170.0),
    (200.0, 200.0),
]


class PiecewiseLinearCorrector:
    # TODO: implémentez le constructeur
    # Il doit accepter table (list[tuple[float, float]]) en paramètre.
    # Assurez-vous que la table contient au moins 2 points.
    pass

    # TODO: implémentez la méthode correct(raw_value)
    # 1. Si raw_value est en dessous du premier point, retourner la première valeur réelle (clamp).
    # 2. Si raw_value est au dessus du dernier point, retourner la dernière valeur réelle (clamp).
    # 3. Sinon, trouver les deux points encadrants et interpoler linéairement :
    #    t = (raw_value - x0) / (x1 - x0)
    #    return y0 + t * (y1 - y0)


def main():
    corrector = PiecewiseLinearCorrector(CALIBRATION_TABLE)
    for sensor_value in range(5, 206, 10):
        sensor = FakeNonlinearUltrasoundSensor(sensor_value)
        raw = sensor.read()
        corrected = corrector.correct(raw)
        print(f"Distance réelle : {sensor_value:3d} cm   ->   Brut : {raw:6.1f}   ->   Corrigé : {corrected:6.1f} cm")


if __name__ == "__main__":
    main()
