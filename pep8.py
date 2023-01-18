
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
# https://peps.python.org/pep-0008/

# variables en minuscule avec underscore
fuel_level = "1"
# courantes en majuscule avec underscore
FIRST_DAY_WEEK = "Monday"
# classe en CapitalizedCase
class BigDog:
    pass
# nom de modules en minuscule en evitant les underscore
import os
import pathlib # contraction de “path” et “lib”

# Commenter le code
    # Mettez les commentaires à jour lorsque le code change.
    # Évitez les commentaires sur la même ligne que le code, ils font négligé.
    # Mettez un seul espace entre le symbole dièse et le texte (pour différencier du code qui a été commenté).
    # Utilisez le même niveau d’indentation que la ligne de code qui suit, pour une bonne lisibilité

# Utiliser le docstrings --> avec 3 quotes """ ... """
    # Selon la PEP 257, il est bon d’utiliser les docstrings partout. (Surtout les classes publiques).
    # commentaires spéciaux écrits au tout début d’une fonction, d’une classe ou d’un module, et utilisés pour la documentation
    # Permets aux outils automatisés d’accéder au texte, par exemple pour générer une documentation en ligne de votre code.
    # Notez que la docstring ne doit jamais décrire le fonctionnement interne de sa fonction ou méthode, mais seulement son retour. Il ne s’agit pas ici d’expliquer le code, mais d’expliquer son usage. C’est tout son intérêt.
    # Decrire retour, paramètres et exceptions
def multiply(first, second=1):
    """Multiply two numbers.

    Args:
        first -- the first number
        second -- the second one (default 1)
    """
    return first * second

print(multiply(13, 77))
# Les docstrings en début de fonction ou de classe sont spéciales, et on peut y accéder en utilisant l’attribut  __doc__  :
print(multiply.__doc__)
def search_film(name):
    """Cherche un film selon un nom donné.

    Attrs:
    - name (str): le nom utilisé pour la recherche.

    Returns:
    - un objet `film` si un film a été trouvé, ou None.
    """
    # ...

# En Python, rien n’est vraiment privé. Mais préfixer vos méthodes d’un underscore pour signaler qu’elles sont privées.
