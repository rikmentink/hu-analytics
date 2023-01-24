#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 3: statistiek

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
naam = "Rik Mentink"
klas = "V1D"
studentnummer = 1829028


def mean(lst):
    """
    Bereken het gemiddelde van alle getallen in een lijst door de somv an alle
    getallen te delen door het aantal getallen.

    1. Bereken de som van alle getallen in de lijst.
    2. Bereken het aantal getallen in de lijst.
    3. Deel de som van alle getallen door het aantal getallen.

    :param lst: De lijst om het gemiddelde van te nemen
    :return: Het gemiddelde van lst
    """
    return sum(lst) / len(lst)


def rnge(lst):
    """
    Bereken het bereik van een gegeven lijst door het minimumgetal van het
    maximumgetal af te halen.

    1. Bereken het grootste getal in de lijst.
    2. Bereken het kleinste getal in de lijst.
    3. Trek het kleinste getal van het grootste getal af.

    :param lst: De lijst om het bereik van te nemen
    :return: Het bereik van lst
    """
    return max(lst) - min(lst)


def median(lst):
    """
    Berekent de mediaan van de lijst. Als de mediaan 2 getallen bevat dan pakt
    hij het gemiddelde van die 2 getallen, en anders het middelste getal.

    1. Sorteer de lijst.
    2. Bereken de index van het midden van de lijst en return het getal dat
        op deze plek staat.
    3. Als de lijst een even aantal getallen heeft, wordt het gemiddelde van
        de 2 middelste getallen teruggegeven.

    :param lst: De lijst om de mediaan van te nemen
    :return: De mediaan van lst
    """
    lst.sort()

    if len(lst) % 2 == 0:
        midden1 = lst[len(lst) // 2]
        midden2 = lst[len(lst) // 2 - 1]
        return float((midden1 + midden2) / 2)
    else:
        return float(lst[len(lst) // 2])


def q1(lst):
    """
    Geeft het eerste kwartiel van een gegeven lijst, door de mediaan
    van de eerste helft van de lijst te berekenen.

    1. Sorteer de lijst.
    2. Bereken de mediaan van de eerste helft van de lijst.

    :param lst: De lijst om het eerste kwartiel van te nemen
    :return: Het eerste kwartier van lst
    """
    lst.sort()
    return median(lst[:len(lst) // 2])


def q3(lst):
    """
    Geeft het derde kwartiel van een gegeven lijst, door de mediaan
    van de tweede helft van de lijst te berekenen.

    1. Sorteer de lijst.
    2. Bereken de mediaan van de tweede helft van de lijst.
    3. Als de lijst een oneven aantal getallen heeft, wordt de index met 1
        opgeschoven.

    :param lst: De lijst om het derde kwartiel van te nemen
    :return: Het derde kwartiel van lst
    """
    lst.sort()

    if len(lst) % 2 == 0:
        return median(lst[(len(lst) // 2):])
    else:
        return median(lst[(len(lst) // 2) + 1:])


def var(lst):
    """
    Bereken de variantie van een gegeven lijst door voor ieder getal het
    verschil met het gemiddelde te kwadrateren, al deze waarden bij elkaar op
    te tellen, en dit vervolgens te delen door het aantal getallen.

    1. Trek van ieder getal het gemiddelde van lst af, en kwadrateer dit getal
    2. Deel de som van al deze waarden door het aantal getallen.

    :param lst: De lijst om de variantie van te berekenen
    :return: De variantie van lst
    """
    return sum((i - mean(lst)) ** 2 for i in lst) / len(lst)


def std(lst):
    """
    Bereken de standaardafwijking van een gegeven lijst door de
    wortel van de variantie te nemen.

    1. Bereken de variantie van de gegeven lijst m.b.v. de var() functie.
    2. Bereken de wortel van de variantie.

    :param lst: De lijst om de standaardafwijking van te berekenen
    :return: De standaardafwijking van lst
    """
    return var(lst) ** 0.5


def freq(lst):
    """
    Bereken de frequenties van alle getallen in een gegeven lijst
    door bij ieder getal te berekenen hoe vaak hij voor komt. Alle
    gegevens worden bij elkaar in een dictionary gezet.

    1. Maak een lege dictionary aan voor alle frequenties.
    2. Loopt door alle getallen heen. Als deze reeds is toegevoegd aan de dict
        wordt het aantal met 1 verhoogd, anders wordt hij toegevoegd.

    :param lst: De lijst om de frequenties van te berekenen
    :return: Een dictionary met alle getallen en hun frequenties
    """
    freqs = dict()

    for num in lst:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    return freqs


def modes(lst):
    """
    Bereken alle modi van een gegeven lijst door alle frequenties te
    berekenen en deze aan een lijst toe te voegen, die tot slot
    gesorteerd wordt.

    1. Bereken de frequenties van de lijst m.b.v. de freq() functie.
    2. Loopt door de frequenties heen, en zet steeds het element met de
        grootste frequentie in de modi lijst.
    3. Sorteer de lijst met modi.

    :param lst: De lijst om alle modi van te berekenen
    :return: Lijst met alle modi van lst
    """
    modi = []
    freqs = freq(lst)

    for num, frequency in freqs.items():
        if frequency == max(freqs.values()):
            modi.append(num)
    return sorted(modi)

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(mean, case[0], case[1])


def test_mean_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mean, (lst_test,), statistics.mean(lst_test), False)


def test_rnge():
    testcases = [
        (([4, 2, 5, 8, 6],), 6),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 5)
    ]

    for case in testcases:
        __my_assert_args(rnge, case[0], case[1])


def test_median():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 4, 6, 4, 2],), 3.5),
        (([1, 3, 4, 6, 2, 4, 2],), 3.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.5)
    ]

    for case in testcases:
        __my_assert_args(median, case[0], case[1])


def test_median_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(median, (lst_test,), statistics.median(lst_test), False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0)

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0)

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])


def test_var():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.25)
    ]

    for case in testcases:
        __my_assert_args(var, case[0], case[1])


def test_var_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(var, (lst_test,), statistics.pvariance(lst_test), False)


def test_std():
    testcases = [
        (([4, 2, 5, 8, 6],), 2.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 1.5)
    ]

    for case in testcases:
        __my_assert_args(std, case[0], case[1])


def test_std_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(std, (lst_test,), statistics.pstdev(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 4, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modes():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modes, case[0], case[1])

def test_modes_simulated():
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        import random
        import statistics
        for lst_size in range(1, 11):
            lst_test = [random.choice(range(5)) for _ in range(lst_size)]
            __my_assert_args(modes, (lst_test,), sorted(statistics.multimode(lst_test)))


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_mean()
        test_mean_simulated()
        print("Je functie mean(lst) werkt goed!")

        test_rnge()
        print("Je functie rnge(lst) werkt goed!")

        test_median()
        test_median_simulated()
        print("Je functie median(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        test_var_simulated()
        print("Je functie var(lst) werkt goed!")

        test_std()
        test_std_simulated()
        print("Je functie std(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modes()
        test_modes_simulated()
        print("Je functie modes(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

        def hist(freqs):
            v_min = min(freqs.keys())
            v_max = max(freqs.keys())

            histo = str()
            for i in range(v_min, v_max + 1):
                histo += "{:5d} ".format(i)
                if i in freqs.keys():
                    histo += "█" * freqs[i]
                histo += '\n'

            return histo

        print("\x1b[0m")
        s = input("Geef een reeks van gehele getallen (gescheiden door een spatie): ")
        userlst = [int(c) for c in s.split()]

        print("\nHet gemiddelde is {:.2f}".format(mean(userlst)))
        print("De modi zijn {}".format(modes(userlst)))
        print("De mediaan is {:.2f}".format(median(userlst)))
        print("Q1 is {:.2f}".format(q1(userlst)))
        print("Q3 is {:.2f}".format(q3(userlst)))

        print("Het bereik is {}".format(rnge(userlst)))
        print("De variantie is {:.2f}".format(var(userlst)))
        print("De standaardafwijking is {:.2f}".format(std(userlst)))

        print("\nHistogram (gekanteld):\n\n" + hist(freq(userlst)))

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()