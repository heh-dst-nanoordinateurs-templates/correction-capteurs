# Exercice 4 — Calibration d'un potentiomètre

## Contexte

Votre potentiomètre est lu via un convertisseur analogique-numérique (ADC).
Les valeurs brutes ne sont pas des pourcentages : elles dépendent des limites mécaniques
et électriques du composant, qui varient d'un exemplaire à l'autre.

Avant de pouvoir utiliser le capteur, il faut le **calibrer** : mesurer ses valeurs brutes
aux deux butées (0 % et 100 %), puis normaliser toutes les lectures suivantes.

Le fichier `fake_potentiometer.py` simule ce potentiomètre. Ne le modifiez pas.
Il expose les méthodes suivantes :

- `set_position()` : change la position physique du potentiomètre
- `read()` : retourne une lecture brute à la position courante
- `sweep()` : retourne une liste de lectures simulant un balayage complet (0 % -> 100 %)

## Partie 1 — Calibration et normalisation

Dans `exercice.py`, implémentez une classe `PotentiometerCalibrator` qui :

1. prend `raw_min` et `raw_max` en paramètres du constructeur (les valeurs brutes aux deux butées)
2. expose une méthode `normalize(raw_value)` qui :
   - mappe la valeur brute vers une plage `[0.0, 100.0]`
   - ramène aux bornes toute valeur hors plage (clamp)

Implémentez aussi une fonction `calibrate(sensor)` qui :

1. appelle `sensor.sweep()` pour observer les valeurs brutes min et max
2. construit et retourne un `PotentiometerCalibrator` avec ces bornes

Vérifiez en lançant `uv run exercice.py` : après calibration, les valeurs affichées doivent être proches de `[0 %, 100 %]`.

Si vous n'utilisez pas `uv`, lancez `python3 exercice.py`.

## Partie 2 — Tests unitaires

Dans `test_exercice.py`, écrivez au moins 3 tests pytest pour `PotentiometerCalibrator.normalize()`.

Couvrez notamment :

- la valeur brute min -> doit donner 0.0 %
- la valeur brute max -> doit donner 100.0 %
- une valeur intermédiaire connue (ex. : milieu de plage -> 50.0 %)

Lancez les tests avec :

```bash
uv run pytest
```

si `uv` est installé sur votre machine.
Ou installez la librairie `pytest` sur votre machine puis exécutez

```bash
pytest
```

Tous les tests doivent être verts avant de passer à l'exercice suivant.

## Ce qu'on attend

| Fichier                 | À modifier ? | Contenu attendu                             |
| ----------------------- | ------------ | ------------------------------------------- |
| `fake_potentiometer.py` | Non          | Stub fourni, boîte noire                    |
| `exercice.py`           | Oui          | Classe `PotentiometerCalibrator` + `main()` |
| `test_exercice.py`      | Oui          | Tests pytest pour `PotentiometerCalibrator` |
