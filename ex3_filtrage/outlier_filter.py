from fake_ultrasound_with_outliers import FakeUltrasoundSensor


class OutlierFilter:
    # TODO: implémentez le constructeur
    # Il doit accepter min_valid et max_valid en paramètres (avec des valeurs par défaut).
    # Pensez à initialiser un attribut pour mémoriser la dernière valeur valide.
    pass

    # TODO: implémentez la méthode update(raw_value)
    # Si raw_value est dans [min_valid, max_valid], mettez à jour la dernière valeur valide.
    # Retournez toujours la dernière valeur valide (ou None si aucune n'a encore été reçue).


def main():
    sensor = FakeUltrasoundSensor(true_distance=50.0, outlier_prob=0.2)
    filtre = OutlierFilter(min_valid=2.0, max_valid=400.0)
    for _ in range(15):
        raw = sensor.read()
        result = filtre.update(raw)
        if result is not None:
            print(f"Brut : {raw:6.1f} cm   -> Dernière valide : {result:.1f} cm")
        else:
            print("Aucune mesure valide reçue")


if __name__ == "__main__":
    main()
