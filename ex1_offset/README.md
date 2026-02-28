# Exercice 1 — Correction d'offset

## Contexte

Votre capteur de température renvoie des valeurs systématiquement trop élevées.
Ce n'est pas du bruit — c'est une erreur **constante et reproductible** : un offset.

Le fichier `fake_temperature.py` simule ce capteur. Ne le modifiez pas.

## Partie 1 — Correction

Dans `exercice.py`, implémentez une classe `OffsetCorrector` qui :

1. prend l'offset connu en paramètre du constructeur
2. expose une méthode `correct(raw_value)` qui retourne la valeur corrigée

Vérifiez votre correction en ouvrant un terminal dans le bon dossier et en lançant `uv run exercice.py` directement :
les valeurs corrigées doivent se situer dans la plage `[16.0, 35.0]`.

Si vous n'utilisez pas `uv`, lancez `python3 exercice.py`.

## Partie 2 — Tests unitaires

Dans `test_exercice.py`, écrivez au moins 3 tests pytest pour `OffsetCorrector.correct()`.

Couvrez notamment :

- le cas nominal (offset positif)
- un offset nul (la valeur doit passer inchangée)
- un cas aux limites de votre choix

Ouvrez un terminal dans le bon dossier et lancez les tests avec :

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

| Fichier               | À modifier ? | Contenu attendu                     |
| --------------------- | ------------ | ----------------------------------- |
| `fake_temperature.py` | Non          | Stub fourni, boîte noire            |
| `exercice.py`         | Oui          | Classe `OffsetCorrector` + `main()` |
| `test_exercice.py`    | Oui          | Tests pytest pour `OffsetCorrector` |
