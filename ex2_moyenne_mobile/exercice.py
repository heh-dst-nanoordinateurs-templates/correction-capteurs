from fake_ultrasound import FakeUltrasoundSensor


class MovingAverage:
    # TODO: implémentez le constructeur
    # Il doit accepter window_size (int) en paramètre.
    # Astuce : vous aurez besoin d'une structure pour stocker les dernières mesures.
    pass

    # TODO: implémentez la méthode update(new_value)
    # Elle doit ajouter new_value à la fenêtre et retourner la moyenne courante.


def main():
    sensor = FakeUltrasoundSensor(true_distance=50.0, noise_std=8.0)
    smoother = MovingAverage(window_size=5)  # TODO: ajustez window_size si besoin
    for _ in range(15):
        raw = sensor.read()
        smoothed = smoother.update(raw)
        print(f"Brut : {raw:6.1f} cm   |   Lissé (N=5) : {smoothed:6.1f} cm")


if __name__ == "__main__":
    main()
