# Exercice 5 (bonus) — Correction de non-linéarité

## Contexte

Votre capteur ultrason a une réponse **non-linéaire** : la valeur brute qu'il retourne
ne correspond pas à la distance réelle via une simple soustraction ou multiplication.
La relation entre brut et réel suit une courbe.

Pour corriger cela, on dispose d'une **table de calibration** : quelques points mesurés
avec un instrument de référence. Entre ces points, on interpole linéairement.

Le fichier `fake_ultrasound_nonlinear.py` simule ce capteur. Ne le modifiez pas.
Les valeurs qu'il retourne ne sont pas en centimètres.

## Partie 1 — Interpolation linéaire par morceaux

Dans `piecewise_linear_corrector.py`, une constante `CALIBRATION_TABLE` est fournie.
C'est une liste de tuples `(valeur_brute, distance_réelle_cm)` triés par valeur brute croissante.

Implémentez une classe `PiecewiseLinearCorrector` qui :

1. prend la table de calibration en paramètre du constructeur
2. expose une méthode `correct(raw_value)` qui :
   - trouve les deux points de calibration encadrant `raw_value`
   - interpole linéairement entre ces deux points
   - ramène aux bornes les valeurs hors de la plage de la table (clamp)

**Rappel — interpolation linéaire** entre deux points `(x0, y0)` et `(x1, y1)` :

```python
t = (raw - x0) / (x1 - x0)
corrected = y0 + t * (y1 - y0)
```

Vérifiez en lançant `uv run piecewise_linear_corrector.py` : pour une distance réelle de 80 cm, les valeurs corrigées doivent être proches des valeurs réelles.

Si vous n'utilisez pas `uv`, lancez `python3 piecewise_linear_corrector.py`.

## Partie 2 — Tests unitaires

Dans `test_piecewise_linear_corrector.py`, écrivez au moins 3 tests pytest pour `PiecewiseLinearCorrector.correct()`.

Couvrez notamment :

- une valeur exactement sur un point de calibration
- une valeur intermédiaire entre deux points (résultat attendu calculable à la main)
- une valeur hors plage (clamp aux bornes)

Lancez les tests avec :

```bash
uv run pytest
```

si `uv` est installé sur votre machine.
Ou installez la librairie `pytest` sur votre machine puis exécutez

```bash
pytest
```

## Ce qu'on attend

| Fichier                              | À modifier ? | Contenu attendu                              |
| ------------------------------------ | ------------ | -------------------------------------------- |
| `fake_ultrasound_nonlinear.py`       | Non          | Stub fourni, boîte noire                     |
| `piecewise_linear_corrector.py`      | Oui          | Classe `PiecewiseLinearCorrector` + `main()` |
| `test_piecewise_linear_corrector.py` | Oui          | Tests pytest pour `PiecewiseLinearCorrector` |
