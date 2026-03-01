from fake_potentiometer import FakePotentiometer


class PotentiometerCalibrator:
    # TODO: implémentez le constructeur
    # Il doit accepter raw_min et raw_max en paramètres.
    pass

    # TODO: implémentez la méthode normalize(raw_value)
    # Elle doit mapper raw_value vers [0.0, 100.0] via une interpolation linéaire.
    # Les valeurs hors plage doivent être ramenées aux bornes (clamp).
    # Rappel — formule : (raw_value - raw_min) / (raw_max - raw_min) * 100.0


# TODO: implémentez la fonction calibrate(sensor)
# Elle doit appeler sensor.sweep() pour trouver les valeurs brutes min et max,
# puis construire et retourner un PotentiometerCalibrator avec ces bornes.
def calibrate(sensor: FakePotentiometer) -> PotentiometerCalibrator:
    pass


def main():
    sensor = FakePotentiometer()

    print("Calibration en cours (balayage complet)...")
    calibrator = calibrate(sensor)
    print("Calibration terminée.\n")

    for i in range(11):
        sensor.set_position(i / 10.0)
        raw = sensor.read()
        percent = calibrator.normalize(raw)
        print(f"Brut : {raw:8.1f}   ->   Position : {percent:5.1f} %")


if __name__ == "__main__":
    main()
