#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: zoeken

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def linear_search(lst, target):
    """
    Bekijkt lineair of target zich in list bevindt.

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: Zit target in lst?
    """
    for element in lst:
        if element == target:
            return True
    return False


def linear_search_index(lst, target):
    """
    Bekijk lineair of target zich in list bevindt. Returned vervolgens de
    index van dit getal

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: Index van target in lst, of -1 als deze zich hier niet bevindt.
    """
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1


def binary_search(lst, target):
    """
    Binair zoek algoritme, neemt steeds het middelste getal en controleert of
    target zich links of rechts hiervan bevindt. Gaat zo door tot hij target
    gevonden heeft.

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: Zit target in lst?
    """
    min = 0
    max = len(lst) - 1

    while min <= max:
        middle = (max + min) // 2

        if lst[middle] < target:
            min = middle + 1
        elif lst[middle] > target:
            max = middle - 1
        else:
            return True
    return False


def binary_search_index(lst, target):
    """
    Binair zoek algoritme, neemt steeds het middelste getal en controleert of
    target zich links of rechts hiervan bevindt. Gaat zo door tot hij target
    gevonden heeft.

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: De index van target in lst, of -1 als deze zich hier niet
             bevindt.
    """
    min = 0
    max = len(lst) - 1

    while min <= max:
        middle = (max + min) // 2

        if lst[middle] < target:
            min = middle + 1
        elif lst[middle] > target:
            max = middle - 1
        else:
            return middle
    return -1


def linear_search_index_steps(lst, target):
    """
    Bekijk lineair of target zich in list bevindt. Returned vervolgens de
    index van dit getal en het aantal stappen het algoritme hiervoor nodig had

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: Tuple met index van target in lst, of -1 als deze zich hier niet
             bevindt, en het aantal benodigde stappen.
    """
    index = 0
    steps = 0

    for i, element in enumerate(lst):
        steps += 1
        if element == target:
            index = i
            return index, steps
    return -1, steps


def binary_search_index_steps(lst, target):
    """
    Binair zoek algoritme, neemt steeds het middelste getal en controleert of
    target zich links of rechts hiervan bevindt. Gaat zo door tot hij target
    gevonden heeft. Houdt ook het aantal benodigde stappen bij.

    :param lst: Lijst om doorheen te zoeken
    :param target: Het doel element
    :return: Tuple met de index van target in lst, of -1 als deze zich hier
             niet bevindt, en het aantal benodigde stappen.
    """
    min = 0
    max = len(lst) - 1
    steps = 0

    while min <= max:
        middle = (max + min) // 2
        steps += 1

        if lst[middle] < target:
            min = middle + 1
        elif lst[middle] > target:
            max = middle - 1
        else:
            return middle, steps
    return -1, steps


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_linear_search():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.randrange(20)
        assert linear_search(lst_test, target) == (target in lst_test), \
            f"Fout: linear_search({lst_test}, {target}) geeft {linear_search(lst_test, target)} " \
            f"in plaats van {target in lst_test}"


def test_linear_search_index():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index(lst_test, target) == lst_test.index(target), \
            f"Fout: linear_search_index({lst_test}, {target}) geeft {linear_search_index(lst_test, target)} " \
            f"in plaats van {lst_test.index(target)}"

        lst_test = [0, 1, 2]
        assert linear_search_index(lst_test, 3) == -1, f"Fout: linear_search_index({lst_test}, {3}) geeft " \
                                                       f"{linear_search_index(lst_test, 3)} in plaats van {-1}"


def test_linear_search_index_steps():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index_steps(lst_test, target)[0] == lst_test.index(target), \
            f"Fout: linear_search_index_steps({lst_test}, {target}) geeft " \
            f"{linear_search_index_steps(lst_test, target)[0]} in plaats van {lst_test.index(target)}"


def test_binary_search():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.randrange(20)
        assert binary_search(lst_test, target) == (target in lst_test), \
            f"Fout: binary_search({lst_test}, {target}) geeft {binary_search(lst_test, target)} " \
            f"in plaats van {target in lst_test}"


def test_binary_search_index():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index(lst_test, target) == lst_test.index(target), \
            f"Fout: binary_search_index({lst_test}, {target}) geeft {binary_search_index(lst_test, target)} " \
            f"in plaats van {lst_test.index(target)}"

        lst_test = [0, 1, 2]
        assert binary_search_index(lst_test, 3) == -1, \
            f"Fout: binary_search_index({lst_test}, {3}) geeft {binary_search_index(lst_test, 3)} in plaats van {-1}"


def test_binary_search_index_steps():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index_steps(lst_test, target)[0] == lst_test.index(target), \
            f"Fout: binary_search_index_steps({lst_test}, {target}) geeft " \
            f"{binary_search_index_steps(lst_test, target)[0]} in plaats van {lst_test.index(target)}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_linear_search()
        print("Je functie linear_search() werkt goed!")

        test_linear_search_index()
        print("Je functie linear_search_index() werkt goed!")

        test_binary_search()
        print("Je functie binary_search() werkt goed!")

        test_binary_search_index()
        print("Je functie binary_search_index() werkt goed!")

        test_linear_search_index_steps()
        print("Je functie linear_search_index_steps() werkt goed!")

        test_binary_search_index_steps()
        print("Je functie binary_search_index_steps() werkt goed!")

        print("\x1b[0m")
        size = int(input("Geef een grootte voor de lijst: "))
        lst_input = list(range(size))
        print("Ik ga zoeken in:", lst_input)
        tgt = int(input("Geef een getal: "))

        (idx, cnt) = linear_search_index_steps(lst_input, tgt)
        print(f"Het lineair zoekalgoritme vond '{tgt}' op index '{idx}' na {cnt} stappen.")

        (idx, cnt) = binary_search_index_steps(lst_input, tgt)
        print(f"Het binair zoekalgoritme vond '{tgt}' op index '{idx}' na {cnt} stappen.")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur