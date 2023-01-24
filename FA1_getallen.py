#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 1: getallen

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Werk onderstaande functies uit.
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


def is_even(n):
    """
    Deelt het getal door 2, en als het overige 0 is is het een even getal.

    :param n: Getal om te controleren
    :return: True of False
    """
    return n % 2 == 0


def floor(real):
    """
    Rond het reële getal naar beneden af.

    :param real: Reëel getal.
    :return: Floor-waarde van real
    """
    return int(real // 1)


def ceil(real):
    """
    Maakt het reële getal negatief en rond het daarna af naar beneden. Door het
    getal weer positief te maken heb je de ceil-waarde.

    :param real: Reëel getal
    :return:
    """
    return int(-(-real // 1))


def div(n):
    """
    Loopt door alle getallen tussen 1 en variabele n. Als het getal deelbaar
    is door n, is het een deler van n. Dan wordt deze aan de lijst divisors
    toegevoegd.

    :param n: Geheel getal
    :return: Lijst met delers van n
    """
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)


def is_prime(n):
    """
    Controleert of het getal een priemgetal is. Als het getal deelbaar is door
    1 en zichzelf, en dit getal groter is dan 1, is het een priemgetal.

    :param n: Geheel getal
    :return: True of False
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def primes(num):
    """
    Berekent alle priemgetallen kleiner dan variabele num. Loopt door ieder
    getal tussen 2 en num, en controleert of dit een priemgetal is. Zo ja,
    dan wordt het aan de lijst primelist toegevoegd.

    :param num: Getal als einde range
    :return: Lijst van priemgetallen kleiner dan num
    """

    primelist = []
    for i in range(2, num):
        if is_prime(i):
            primelist.append(i)
    return sorted(primelist)


def primefactors(n):
    """
    Berekent alle priemfactoren van variabele n. Deelt steeds n door een zo
    klein mogelijk getal, tot er niks meer van n over is. Alle getallen (i)
    waardoor hij gedeeld is worden aan een lijst toegevoegd. Dit zijn de
    priemfactoren van n.

    :param n: Geheel getal om priemfactoren van te bepalen
    :return: Lijst met priemfactoren van n
    """
    factors = []
    i = 2

    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    return sorted(factors)


def gcd(a, b):
    """
    Berekent de grootste gemene deler van getal a en b m.b.v. het Algoritme
    van Euclides:
        1. Trek B zo vaak van A af tot er 0 overblijft (a % b)
        2. Als 0 overblijft is B de ggd, anders herhalen met B en wat er van A over is.

    :param a: Getal 1
    :param b: Getal 2
    :return: De grootste gemene deler van a en b
    """
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    """
    Bepaalt de kleinste gemene veelvoud van getal a en b door de absolute
    waarde van a x b te delen door de ggd van a en b.

    :param a: Getal 1
    :param b: Getal 2
    :return: De kleinste gemene veelvoud van a en b
    """
    return abs(a * b) // gcd(a, b)


def add_frac(n1, d1, n2, d2):
    """
    Telt 2 breuken bij elkaar op volgens de volgende stappen:
        1. De nieuwe teller bepalen. Beide oude tellers worden vermenigvuldigd
           met de KGV van de noemers, en vervolgens bij elkaar opgeteld.
        2. De nieuwe noemer bepalen. Deze wordt de KGV van de noemers.
        3. Vereenvoudigen van de breuk. Dit doen we door de nieuwe teller en
           noemer te delen door de GGD van de nieuwe teller en noemer.

    :param n1: Teller van breuk 1
    :param d1: Noemer van breuk 1
    :param n2: Teller van breuk 2
    :param d2: Noemer van breuk 2
    :return: Tuple met de teller en noemer van de nieuwe breuk
    """
    xverm = (n1 * lcm(d1, d2) // d1) + (n2 * lcm(d1, d2) // d2)
    teller = xverm // gcd(xverm, lcm(d1, d2))
    noemer = lcm(d1, d2) // gcd(xverm, lcm(d1, d2))

    return (teller, noemer)
