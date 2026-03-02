# Exercice 2 — Moyenne mobile

## Contexte

Votre capteur ultrason renvoie des valeurs bruitées : chaque mesure fluctue aléatoirement autour de la vraie distance.
Ce n'est pas une erreur constante — c'est un bruit imprévisible à chaque lecture.

Le fichier `fake_ultrasound_with_noise.py` simule ce capteur. Ne le modifiez pas.

## Partie 1 — Lissage

Dans `moving_average.py`, implémentez une classe `MovingAverage` qui :

1. prend la taille de la fenêtre `window_size` en paramètre du constructeur
2. expose une méthode `update(new_value)` qui :
   - ajoute la nouvelle mesure à la fenêtre
   - retourne la **moyenne** des valeurs actuellement dans la fenêtre
3. ne conserve que les `window_size` dernières mesures (les plus anciennes sont oubliées)

Vérifiez votre lissage en lançant `uv run moving_average.py` :
les valeurs lissées doivent être nettement plus stables que les valeurs brutes.

Si vous n'utilisez pas `uv`, lancez `python3 moving_average.py`.

## Partie 2 — Tests unitaires

Dans `test_moving_average.py`, écrivez au moins 3 tests pytest pour `MovingAverage.update()`.

Couvrez notamment :

- une fenêtre de taille 1 (le résultat doit être égal à la dernière valeur)
- la moyenne de deux valeurs connues
- le comportement glissant : après avoir rempli la fenêtre, une nouvelle valeur doit faire sortir la plus ancienne

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

| Fichier                         | À modifier ? | Contenu attendu                   |
| ------------------------------- | ------------ | --------------------------------- |
| `fake_ultrasound_with_noise.py` | Non          | Stub fourni, boîte noire          |
| `moving_average.py`             | Oui          | Classe `MovingAverage` + `main()` |
| `test_moving_average.py`        | Oui          | Tests pytest pour `MovingAverage` |
