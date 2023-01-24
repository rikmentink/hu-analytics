#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: selection sort

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def swap(lst, index1, index2):
    """
    Verwisselt de elementen op index1 en index2 in lst.

    :param lst: de lijst die moet worden gesorteerd
    :param index1: de index van het eerste item dat moet worden verwisseld
    :param index2: de index van het item dat verplaatst moet worden
    :return: De lijst met de twee elementen verwisseld.
    """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


def find_index_of_minimum(lst, start_index=0):
    """
    Vindt de index van de minimumwaarde in een lijst, beginnend bij een
    bepaalde index.

    :param lst: de lijst om in te zoeken
    :param start_index: de index van het eerste element waarmee rekening moet
                        worden gehouden, hij is standaard 0
    :return: De index van de minimumwaarde in de lijst.
    """
    minimum = lst[start_index]
    index_of_minimum = start_index

    for i, num in enumerate(lst, start_index):
        if num < minimum:
            minimum = num
            index_of_minimum = i

    return index_of_minimum


def selection_sort(lst):
    """
    Zoek voor elke index in de lijst de index van de minimumwaarde, beginnend
    bij die index, en verwissel de minimumwaarde met de waarde van de huidige
    index.

    De eerste regel van de functie maakt een kopie van de lijst. Dit doen we
    omdat we de oorspronkelijke lijst niet willen wijzigen.

    :param lst: de lijst die gesorteerd moet worden
    :return: De gesorteerde lijst.
    """
    lst_sorted = lst.copy()

    for i in range(len(lst_sorted)):
        min_index = find_index_of_minimum(lst_sorted[i:]) + i
        swap(lst_sorted, min_index, i)

    return lst_sorted


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_swap():
    lst_test = [4, 9, 7]
    swap(lst_test, 0, 1)
    assert lst_test == [9, 4, 7], "Fout: swap([4, 9, 7], 0, 1) geeft {} in plaats van {}".format(lst_test, [9, 4, 7])

    lst_test = [4, 9, 7]
    swap(lst_test, 1, 2)
    assert lst_test == [4, 7, 9], "Fout: swap([4, 9, 7], 1, 2) geeft {} in plaats van {}".format(lst_test, [4, 7, 9])

    lst_test = [4, 9, 7]
    swap(lst_test, 0, 2)
    assert lst_test == [7, 9, 4], "Fout: swap([4, 9, 7], 0, 2) geeft {} in plaats van {}".format(lst_test, [7, 9, 4])


def test_find_index_of_minimum():
    lst_test = [18, 6, 21, 44, 9, 14]
    assert find_index_of_minimum(lst_test, 0) == 1, \
        f"Fout: find_index_of_minimum({lst_test}, 0) geeft {find_index_of_minimum(lst_test, 0)} in plaats van 1"
    assert find_index_of_minimum(lst_test, 2) == 3, \
        f"Fout: find_index_of_minimum({lst_test}, 2) geeft {find_index_of_minimum(lst_test, 2)} in plaats van 4"
    assert find_index_of_minimum(lst_test, 3) == 4, \
        f"Fout: find_index_of_minimum({lst_test}, 3) geeft {find_index_of_minimum(lst_test, 3)} in plaats van 4"


def test_selection_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = selection_sort(lst_test)

    assert lst_copy == lst_test, "Fout: selection_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: selection_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_swap()
        print("Je functie swap() werkt goed!")

        test_find_index_of_minimum()
        print("Je functie find_index_of_minimum() werkt goed!")

        test_selection_sort()
        print("Je selection sort algoritme werkt goed!\n\nKnap gedaan!\n")

        print("\x1b[0m")
        aantal = int(input("Hoeveel getallen zal ik sorteren? "))
        lijst = random.choices(range(0, 100), k=aantal)

        print(f"De lijst: \n\t{lijst}")
        gesorteerde_lijst = selection_sort(lijst)
        print(f"is na sortering: \n\t{gesorteerde_lijst}")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur