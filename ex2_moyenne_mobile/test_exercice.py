from exercice import MovingAverage


# TODO: écrivez au moins 3 tests pour MovingAverage.update().
#
# Couvrez notamment :
#   - une fenêtre de taille 1 (le résultat doit être égal à la dernière valeur)
#   - la moyenne de deux valeurs connues
#   - le comportement glissant : après avoir rempli la fenêtre, une nouvelle valeur
#     doit faire sortir la plus ancienne
#
# Exemple de structure d'un test pytest :
#
#   def test_mon_cas():
#       ma = MovingAverage(window_size=2)
#       ma.update(10.0)
#       assert ma.update(20.0) == 15.0
