from piecewise_linear_corrector import PiecewiseLinearCorrector


# TODO: écrivez au moins 3 tests pour PiecewiseLinearCorrector.correct().
#
# Conseil : définissez une table simple pour vos tests (pas CALIBRATION_TABLE),
# afin de pouvoir calculer les résultats attendus à la main.
#
# Couvrez notamment :
#   - une valeur exactement sur un point de calibration
#   - une valeur intermédiaire entre deux points (résultat attendu calculable à la main)
#   - une valeur hors plage (clamp aux bornes)
#
# Exemple de structure d'un test pytest :
#
#   TABLE = [(0.0, 0.0), (50.0, 100.0), (100.0, 150.0)]
#
#   def test_mon_cas():
#       c = PiecewiseLinearCorrector(TABLE)
#       assert c.correct(50.0) == 100.0
