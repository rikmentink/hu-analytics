#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: insertion sort

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def insert(lst, grens, waarde):
    """
    Kijkt vanaf de gegeven grens in de lijst of de gegeven waarde groter of
    kleiner is dan de huidige index. Als deze hoger is, schuift de index op.
    Dit wordt herhaald totdat de waarde op de juiste plek in de lijst staat.

    :param lst: De lijst om de waarde in te zetten
    :param grens: De grens om te beginnen met sorteren
    :param waarde: De waarde om in de lijst te zetten
    :return: De lijst met de waarde er in
    """
    i = grens
    while i < len(lst) and lst[i] < waarde:
        i += 1 

    lst.insert(i, waarde)

    return lst


def insertion_sort(lst):
    """
    Een insertion sort algoritme dat de gegeven lijst kopieërt en vervolgens
    sorteerd. Iedere waarde in de lijst wordt één voor één op volgorde in de
    lijst gezet, door telkens te controleren of het getal erna groter is of
    kleiner is.

    :param lst: De lijst om te sorteren
    :return: De lijst gesorteerd
    """
    sorted_list = lst.copy()

    for i in range(1, len(sorted_list)):
        value = sorted_list[i]
        index = i - 1

        while index >= 0 and value < sorted_list[index]:
            sorted_list[index + 1] = sorted_list[index]
            index -= 1
        sorted_list[index + 1] = value
    return sorted_list


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_insert():
    lst_res = [3, 5, 7, 11, 13, 2, 9, 14]
    lst_test = lst_res.copy()
    insert(lst_res, 4, 2)
    lst_correct = [2, 3, 5, 7, 11, 13, 9, 14]
    assert lst_res == lst_correct, \
        f"Fout: insert({lst_test}, 4, 2) geeft {lst_res} in plaats van {lst_correct}"

    lst_test = lst_res.copy()
    insert(lst_res, 5, 9)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        f"Fout: insert({lst_test}, 5, 9) geeft {lst_res} in plaats van {lst_correct}"

    lst_test = lst_res.copy()
    insert(lst_res, 6, 14)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        f"Fout: insert({lst_test}, 6, 14) geeft {lst_res} in plaats van {lst_correct}"


def test_insertion_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = insertion_sort(lst_test)

    assert lst_copy == lst_test, "Fout: insertion_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: insertion_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_insert()
        print("Je functie insert() werkt goed!")

        test_insertion_sort()
        print("Je insertion sort algoritme werkt goed!\n\nKnap gedaan!\n")

        print("\x1b[0m")
        aantal = int(input("Hoeveel elementen zal ik sorteren? "))
        lijst = random.choices(range(0, 100), k=aantal)

        print(f"De lijst: \n\t{lijst}")
        gesorteerde_lijst = insertion_sort(lijst)
        print(f"is na sortering met jouw algoritme: \n\t{gesorteerde_lijst}")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur