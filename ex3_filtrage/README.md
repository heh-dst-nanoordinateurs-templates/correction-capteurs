# Exercice 3 — Filtrage des valeurs aberrantes

## Contexte

Votre capteur ultrason produit de temps en temps des valeurs impossibles : `0 cm` ou `400 cm`.
Ces valeurs ne sont pas du bruit — elles indiquent une **panne momentanée** du capteur.
Les ignorer est préférable à les utiliser pour prendre une décision.

Le fichier `fake_ultrasound.py` simule ce capteur. Ne le modifiez pas.

## Partie 1 — Filtrage

Dans `exercice.py`, implémentez une classe `OutlierFilter` qui :

1. prend les bornes `min_valid` et `max_valid` en paramètres du constructeur
2. expose une méthode `update(raw_value)` qui :
   - met à jour la dernière valeur valide si `raw_value` est dans la plage `[min_valid, max_valid]`
   - retourne **toujours** la dernière valeur valide connue, ou `None` si aucune valeur valide n'a encore été reçue

Vérifiez votre filtre en lançant `uv run exercice.py` :
les sorties doivent toujours afficher la dernière distance valide connue, même après une mesure aberrante.

Si vous n'utilisez pas `uv`, lancez `python3 exercice.py`.

## Partie 2 — Tests unitaires

Dans `test_exercice.py`, écrivez au moins 3 tests pytest pour `OutlierFilter.update()`.

Couvrez notamment :

- une valeur dans la plage (doit mettre à jour et retourner la valeur)
- une valeur aberrante sans mesure valide préalable (doit retourner `None`)
- une valeur aberrante après une mesure valide (doit retourner l'ancienne valeur valide)

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

| Fichier              | À modifier ? | Contenu attendu                   |
| -------------------- | ------------ | --------------------------------- |
| `fake_ultrasound.py` | Non          | Stub fourni, boîte noire          |
| `exercice.py`        | Oui          | Classe `OutlierFilter` + `main()` |
| `test_exercice.py`   | Oui          | Tests pytest pour `OutlierFilter` |
