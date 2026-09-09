"""LU07.A04 - Loesung: die lange Funktion ist in benannte Teilfunktionen zerlegt.

Angewendete Techniken:
  * Replace Magic Number with Named Constant (RABATT_AB_BETRAG, RABATT_PROZENT)
  * Extract Function (ist_gueltig, zeilenwert, kundenname, zeile)
  * Replace Loop with Pipeline (Comprehension statt Schleife, sum statt Akkumulator)
  * f-Strings statt String-Verkettung

Das Verhalten ist unveraendert, main_test.py belegt das.
"""

RABATT_AB_BETRAG = 100
RABATT_PROZENT = 5
STATUS_STORNIERT = 'storniert'

BESTELLUNGEN = [
    {'kunde': '  Meier ', 'artikel': 'Maus', 'menge': 3, 'preis': 25.0, 'status': 'offen'},
    {'kunde': 'keller', 'artikel': 'Laptop', 'menge': 1, 'preis': 1200.0, 'status': 'bezahlt'},
    {'kunde': 'MEIER', 'artikel': 'Tastatur', 'menge': 2, 'preis': 80.0, 'status': 'bezahlt'},
    {'kunde': 'Suter', 'artikel': 'USB-Hub', 'menge': 5, 'preis': 12.0, 'status': 'storniert'},
    {'kunde': 'keller ', 'artikel': 'Monitor', 'menge': 1, 'preis': 210.0, 'status': 'offen'},
]


def ist_gueltig(bestellung):
    """
    Prueft, ob eine Bestellung in den Bericht gehoert.

    :param bestellung: eine einzelne Bestellung
    :return: True, wenn die Bestellung nicht storniert ist
    """
    return bestellung['status'] != STATUS_STORNIERT


def zeilenwert(bestellung):
    """
    Berechnet den Wert einer Bestellung inklusive Mengenrabatt.

    :param bestellung: eine einzelne Bestellung
    :return: der Wert als float, ungerundet
    """
    wert = bestellung['menge'] * bestellung['preis']
    if wert < RABATT_AB_BETRAG:
        return wert
    return wert * (1 - RABATT_PROZENT / 100)


def kundenname(bestellung):
    """
    Vereinheitlicht den Kundennamen fuer die Ausgabe.

    :param bestellung: eine einzelne Bestellung
    :return: der Name ohne Randleerzeichen, mit grossem Anfangsbuchstaben
    """
    return bestellung['kunde'].strip().lower().capitalize()


def zeile(bestellung):
    """
    Formatiert eine einzelne Berichtszeile.

    :param bestellung: eine einzelne Bestellung
    :return: die formatierte Zeile
    """
    artikel = bestellung['artikel']
    return f'{kundenname(bestellung)}: {artikel} = {round(zeilenwert(bestellung), 2)} CHF'


def bericht(bestellungen):
    """
    Erstellt den Bestellbericht als mehrzeiligen String.

    :param bestellungen: Liste von Bestellungen
    :return: der fertige Bericht als String
    """
    gueltige = [b for b in bestellungen if ist_gueltig(b)]
    # Startwert 0.0: sonst liefert sum() bei leerer Liste ein int und der
    # Bericht endet mit "Total: 0 CHF" statt "Total: 0.0 CHF".
    total = round(sum((zeilenwert(b) for b in gueltige), 0.0), 2)
    kopf = f'Bestellungen ({len(gueltige)})'
    strich = '-' * len(kopf)
    return '\n'.join([kopf, strich] + [zeile(b) for b in gueltige] + [strich, f'Total: {total} CHF'])


if __name__ == '__main__':
    print(bericht(BESTELLUNGEN))
