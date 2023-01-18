
# Le code doit permettre d'expliquer à l'ordinateur
# ainsi qu'aux développeur ce qu'il doit faire.

# premier code est concentré, il prend pas beaucoup de ligne
# mais on ne sait pas trop ce qu'il fait. Pas un bon titre + calcule complexifié
def adjustment(value):
    return (value % 4 == 0) and (value % 100 != 0 or value % 400 == 0)

# VS

# Le même code mais là l'humain comprend directement ce qu'il fait.
# Ces deux fonctions sont équivalent pour l'ordinateur mais plus adapté
# et agréable pour les développeurs.
def is_leap_year(year):
    # Les années bissextiles sont toutes des multiples de 4
    if year % 4 != 0:
        return False

    # Les années séculaires ne sont pas bissextiles, hormis 1600, 2000, 2400, etc.
    if year % 100 == 0:
        return year % 400 == 0

    # Tous les autres résultats sont vrais.
    return True


# Ainsi, un guide existe pour faire du code python maintenable : PEP 8
# PEP pour Python Enhancement Proposal (proposition d'amélioration de Python).
