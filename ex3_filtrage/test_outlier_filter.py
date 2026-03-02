from outlier_filter import OutlierFilter


# TODO: écrivez au moins 3 tests pour OutlierFilter.update().
#
# Couvrez notamment :
#   - une valeur dans la plage (doit mettre à jour et retourner la valeur)
#   - une valeur aberrante sans mesure valide préalable (doit retourner None)
#   - une valeur aberrante après une mesure valide (doit retourner l'ancienne valeur valide)
#
# Exemple de structure d'un test pytest :
#
#   def test_mon_cas():
#       f = OutlierFilter(min_valid=2.0, max_valid=400.0)
#       assert f.update(50.0) == 50.0
