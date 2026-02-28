from fake_temperature import FakeTemperatureSensor


class OffsetCorrector:
    # TODO: implémentez le constructeur
    # Il doit accepter l'offset connu en paramètre.
    pass

    # TODO: implémentez la méthode correct(raw_value)
    # Elle doit retourner la valeur corrigée.


def main():
    sensor = FakeTemperatureSensor()
    corrector = OffsetCorrector(offset=???)  # TODO: quelle valeur passer ici ?

    for _ in range(10):
        raw_value = sensor.read()
        corrected = corrector.correct(raw_value)
        print(f"Brut : {raw_value:.2f} °C  |  Corrigé : {corrected:.2f} °C")


if __name__ == "__main__":
    main()
