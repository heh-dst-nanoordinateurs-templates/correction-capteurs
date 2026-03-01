from exercice import PotentiometerCalibrator


# TODO: écrivez au moins 3 tests pour PotentiometerCalibrator.normalize().
#
# Couvrez notamment :
#   - la valeur brute min -> doit donner 0.0 %
#   - la valeur brute max -> doit donner 100.0 %
#   - une valeur intermédiaire connue (ex. : milieu de plage -> 50.0 %)
#
# Exemple de structure d'un test pytest :
#
#   def test_mon_cas():
#       cal = PotentiometerCalibrator(raw_min=0.0, raw_max=1000.0)
#       assert cal.normalize(0.0) == 0.0
