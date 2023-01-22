#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Part 2, design patterns"""
# 3 design patterns utile pour python #

# Design pattern Constant: #
# # Vise a mettre tous les valeurs en constante, pour pouvoir
# # facilement modifier et mieux comprendre le code en meme temps.

# Design pattern Decorator: #
# Creez une fonction decorateur qui :
# # attend une autre fonction en parametre,
# # et retourne une variation decoree de cette fonction en retour.
# Le decorateur n’est qu’un modificateur de fonction.
# Il va la transformer pour rajouter des choses avant, et apres.


def decorate_function_old(function):
    """Cette fonction va générer le décorateur."""

    def wrapper():
        """Voici le "vrai" décorateur.

        C'est ici que l'on change la fonction de base
        en rajoutant des choses avant et après.
        """
        print("Do something at the start")

        result = function()

        print("Do something at the end")

        return result

    return wrapper


def travelling_through_the_stars_old():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")


# ici, nous allons récupérer le retour de "decorate_function",
# qui n'est autre que la fonction "wrapper" !
# Notez que nous pouvons très bien renommer une fonction en
# l'assignant dans une nouvelle variable (ici "wrapper" devient "decorated").
decorated = decorate_function_old(travelling_through_the_stars_old)
decorated()  # nous executons la fonction "wrapper"

# L’une des conséquences regrettables des décorateurs, c’est que 
# vous devez créer une fonction, puis la redéfinir avec le décorateur. 
# Il serait préférable de pouvoir tout faire en une seule étape.
# Avec python, il est possible d'utiliser une systaxe spécifique 
# qui symplifie la vie (on parle de sucre syntaxique)


def decorate_function(function):
    """Cette fonction va générer le décorateur."""

    def wrapper():
        """Le "vrai" décorateur."""
        print("Do something at the start")
        result = function()
        print("Do something at the end")
        return result

    return wrapper


@decorate_function  # c'est ici que ça se passe !
def travelling_through_the_stars():
    """Voyage à travers les étoiles."""
    print("C'est parti pour un long voyage !")


# la fonction est directement décorée, et s'utilise comme telle,
# comme si rien n'avait changé ! ;)
travelling_through_the_stars()

# La syntaxe  @decorate_function  dit à l’interpréteur Python que cette 
# fonction doit être décorée par la fonction décorateur  decorate_function. 
# Très concrètement, l’interpréteur Python va exécuter la fonction 
# décorateur lors du lancement du code, et passer la fonction décorée en 
# paramètre de son appel. Exactement comme pour la première méthode. 
# Ici la fonction garde le même nom, mais représente en fait le “wrapper” 
# retourné par le décorateur.

# Le decorator pourrait être utiliser pour facilement calculer le temps que
# prend une fonction sans modifier cette fonction par exemple : 
from time import time, sleep
 

def calculate_time_spent(function):
    """calcule le temps que met une fonction à s'executer."""
 
    # notez *args et **kwargs. Ce sont des paramètres dynamiques
    # qui permet au décorateur de s'adapter à tout type de fonction !
    # N'hésitez pas à vous documenter sur l'unpacking pour en apprendre
    # davantage.
    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # On appelle cela le temps "epoch".
        start = time()

        result = function()

        # mettez ici votre code. Il s'agit de faire la différence entre
        # 2 temps "epochs", celui qui est gardé dans "start", et celui qui
        # sera gardé dans votre variable 'end'. ;)
        end = # ...
        time_spent = # …
        print(f"secondes passées: {time_spent:.2f}")
 
        return result
 
    return wrapper
 

# n'oubliez pas de décorer la fonction !
def calculate_the_trajectory():
    """Calcule la trajectoire du vaisseau."""
    print("Calcul en cours...")
    sleep(3)  # on met le programme en pause pendant 3 secondes !
    print("Calcul terminé !")
 

calculate_the_trajectory()