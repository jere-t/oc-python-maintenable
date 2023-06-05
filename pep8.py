
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
# constantes en majuscule avec underscore
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
def __custom__(self):
    pass

# Les espaces #
# Le code doit être indenté avec 4 espaces (et non des tabulations).
# Mettez un seul espace autour des opérateurs d’affectation (  is_little = "little" in sanctuary  ) et des opérateurs logiques (  max_places  < 5  ). La seule exception intervient lorsque l’on fixe des valeurs par défaut en paramètres de fonctions et méthodes, telles que  def voiture(color, max_places=4):  .
# Ne laissez jamais d’espaces tout de suite à l’intérieur de parenthèses ou de crochets. Écrivez  (expression)  et  [0]  , pas  ( expression )   ou  [ 0 ]  .
# Ne laissez pas de blanc entre une fonction, comme  print()  , et ses arguments. print(f"test")
# Laissez un espace entre  if  et toute parenthèse. La même règle s’applique à  for  . Ceci vise à être cohérent avec les situations où il n’y a pas de parenthèses.

# Saut de ligne #
# Avant une définition de classe (c’est-à-dire quand vous écrivez  class MyClass  ) ou une définition de fonction (c’est-à-dire quand vous écrivez  def my_function(...):  ), sautez deux lignes.
# Avant une définition de méthode au sein d’une classe, ne sautez qu’une seule ligne.

# Limiter les lignes de code à 79 caractères (plus facile ä suivre et rentre mieux dans les éditeurs).
# Les fonctions avec beaucoup d'argument doivent s'écrire sur plusieurs lignes avec une indentation
# Ces alternatives peuvent être utilisées:
def function_with_a_rather_long_name(parameter_number_1, parameter_number_2,
                                     parameter_number_3):
# Même chose, mais avec un paramètre par ligne
def function_with_a_rather_long_name(parameter_number_1,
                                     parameter_number_2,
                                     parameter_number_3):
# Un paramètre par ligne, et la parenthèse au même niveau d’indentation que la fonction
def function_with_a_rather_long_name(
    parameter_number_1,
    parameter_number_2,
    Parameter_number_3
):

# Organisation du fichier #
# 1.Les commentaires qui concernent la totalité du fichier vont en haut.
# 2.Les imports suivent cet ordre :
#   2.1.Modules de la bibliothèque standard, par exemple  import random  .
#   2.2.Modules de bibliothèques tierces, par exemple  import sklearn  .
#   2.3.Modules locaux, par exemple  import mymodule  .
# 3.Les constantes, par exemple  MY_CONSTANT = 77  .
# 4.Tout autre code

# Écrire du code antibug #

# Faire des retours de fonctions cohérent
    # Soit toutes les instructions  <return>  retournent une valeur, soit aucune ne le fait.
    # Tous les types de retours doivent être les mêmes (sauf s’il y a une très bonne raison de faire autrement !).
    # Utilisez  <return None>  plutôt qu’un  <return>  nu.
def less_confusing_division(top, bottom):
    """Divise "top" par "bottom"."""
    if bottom == 0 or top == 0:
        return None

    if top % bottom != 0:
        return None

    return top / bottom


if less_confusing_division(7, 3) is not None:
    # fait quelque chose
else:
        # fait autre chose

# Écrivez des chaînes cohérentes
# Plutôt qu'écrire ça :
phone_number = "0123456789"
if phone_number[:3] == "012":
    print("Yes!")
# Utiliser les méthodes des types de base
if phone_number.startswith(MY_START_PHONE_NUMBER):
    print("Of course!")
if phone_number.endswith("7890"):
    print("Verily!")
if "345" in phone_number:
    print("Affirmative!")

# Simplifiez les exceptions #
    # Le bloc try doit couvrir le moins de code possible pour éviter de couvrir un autre bug
    # N’utilisez jamais la clause <except> nue, car vous risquez de passer sous silence des erreurs critiques, et vous interférerez avec les exceptions <KeyboardInterrupt> et <SystemExit> , qui servent à arrêter le programme.

def get_number():
    """Get a number input and return it's value."""
    try:
        choice = input(f"Sélectionnez un nombre :")
        number = int(choice)
        return number
    except ValueError: # as error (si besoin de récuperer)
        print(f"{choice} n'est pas un nombre, on retourne None")
        return None

print(f"Le nombre est {get_number()}")

# Suivre les recommandations de programmation #
# https://peps.python.org/pep-0008/#programming-recommendations

# Le plus important : Utiliser un linter pour vérifier automatiquement que PEP8 est respecté
# Le plus connu est Flake8 : https://flake8.pycqa.org/en/latest/
# Un linter online existe aussi : Pep8online

# Des autoformateurs existent aussi pour automatiquement formater le code selon pep-8
# Le plus connu est Black :  https://github.com/psf/black

# poetry : https://github.com/python-poetry/poetry
# mypy : https://github.com/python/mypy
# pydantic (or djantic for django) : typing env 
