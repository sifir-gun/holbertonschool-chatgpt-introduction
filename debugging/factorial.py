#!/usr/bin/python3
"""
Ce module fournit une fonction pour calculer la factorielle d'un nombre.
"""

import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n pour éviter la boucle infinie
    return result


f = factorial(int(sys.argv[1]))
print(f)
