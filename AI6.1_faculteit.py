#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: faculteit (iteratief)

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def faculteit_iteratief(n):
    """
    Bereken de faculteit van n, door steeds de getallen tussen 1 en n met
    elkaar te vermenigvuldigen.

    :param n: Het getal om de faculteit van te berekenen
    :return: De faculteit van n
    """
    res = 1

    for i in range(1, n + 1):
        res *= i

    return res


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math


def test_faculteit_iteratief():
    for x in range(6):
        assert faculteit_iteratief(x) == math.factorial(x), \
            f"Fout: faculteit_iteratief({x}) geeft {faculteit_iteratief(x)} in plaats van {math.factorial(x)}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_faculteit_iteratief()
        print("Je functie faculteit_iteratief() doorstaat de tests!")

        print("\x1b[0m")

        getal = int(input("Geef een getal: "))
        print(f"{getal}! = {faculteit_iteratief(getal)}")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur