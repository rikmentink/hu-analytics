#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: recursie

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def faculteit(n):
    """
    Bereken de faculteit van een gegeven getal op recursieve wijze.

    :param n: Het getal om de faculteit van de berekenen
    :return: De faculteit van n
    """
    if n == 0:
        return 1

    else:
        return n * faculteit(n - 1)


def exponent(n):
    """
    Bereken de exponent van 2 (2^n) van het getal n op recursieve wijze.

    :param n: Het getal om de exponent van 2 van te berekenen
    :return: De exponent van 2 van n
    """
    if n == 0:
        return 1

    return 2 * exponent(n - 1)


def som(lst):
    """
    Bereken de som van alle getallen uit n op recursieve wijze.

    :param lst: De lijst om de som van te berekenen
    :return: De som van alle getallen uit lst
    """
    if len(lst) == 0:
        return 0

    return lst[0] + som(lst[1:])


def palindroom(woord):
    """
    Controleert of een gegeven woord een palindroom is. Als de eerste en de
    laatste letter gelijk zijn, roept hij de functie opnieuw aan, zonder de
    huidige eerste en laatste letter. Zo controleert hij voor het volledige
    woord of de 2 buitenste getallen gelijk zijn. Zodra hij bij het laatste
    getal uitkomt returned hij ook True.

    :param woord: Het woord om te controleren
    :return: Of het woord een palindroom is
    """
    if len(woord) == 0 or len(woord) == 1:
        return True

    if woord[0] != woord[-1]:
        return False

    return palindroom(woord[1:-1])


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math
import random


def test_faculteit():
    for i in range(6):
        assert faculteit(i) == math.factorial(i), \
            f"Fout: faculteit({i}) geeft {faculteit(i)} in plaats van {math.factorial(i)}"


def test_exponent():
    for i in range(10):
        assert exponent(i) == 2**i, \
            f"Fout: exponent({i}) geeft {exponent(i)} in plaats van {2**i}"


def test_som():
    for i in range(6):
        lst_test = random.sample(range(-10, 11), i)
        assert som(lst_test) == sum(lst_test), \
            f"Fout: som({lst_test}) geeft {som(lst_test),} in plaats van {sum(lst_test)}"


def test_palindroom():
    testcases = [
        ("", True),
        ("raar", True),
        ("maandnaam", True),
        ("lekker", False),
        ("radar", True),
        ("pollepel", False),
        ("Maandnaam", False)
    ]

    for testcase, res in testcases:
        assert palindroom(testcase) is res, \
            f"Fout: palindroom({testcase}) geeft {palindroom(testcase)} in plaats van {res}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_faculteit()
        print("Je functie faculteit() doorstaat de tests!")

        test_exponent()
        print("Je functie exponent() doorstaat de tests!")

        test_som()
        print("Je functie som() doorstaat de tests!")

        test_palindroom()
        print("Je functie palindroom() doorstaat de tests!")

        print("\x1b[0m")

        x = input("Geef een woord: ")
        print(f"'{x}' is {'' if palindroom(x) else 'g'}een palindroom!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur