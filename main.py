"""LU07.A04 - Lange Funktion zerlegen.

Die Funktion `bericht` funktioniert korrekt, ist aber schwer zu lesen:
Sie filtert, rechnet, formatiert und baut die Ausgabe in einem Stueck.

Ihre Aufgabe: zerlegen, ohne die Ausgabe zu veraendern.
Die Namen `BESTELLUNGEN` und `bericht` muessen erhalten bleiben.
"""

BESTELLUNGEN = [
    {'kunde': '  Meier ', 'artikel': 'Maus', 'menge': 3, 'preis': 25.0, 'status': 'offen'},
    {'kunde': 'keller', 'artikel': 'Laptop', 'menge': 1, 'preis': 1200.0, 'status': 'bezahlt'},
    {'kunde': 'MEIER', 'artikel': 'Tastatur', 'menge': 2, 'preis': 80.0, 'status': 'bezahlt'},
    {'kunde': 'Suter', 'artikel': 'USB-Hub', 'menge': 5, 'preis': 12.0, 'status': 'storniert'},
    {'kunde': 'keller ', 'artikel': 'Monitor', 'menge': 1, 'preis': 210.0, 'status': 'offen'},
]


def bericht(bestellungen):
    """
    Erstellt den Bestellbericht als mehrzeiligen String.

    :param bestellungen: Liste von Bestellungen
    :return: der fertige Bericht als String
    """
    zeilen = []
    total = 0.0
    anzahl = 0
    for b in bestellungen:
        if b['status'] != 'storniert':
            wert = b['menge'] * b['preis']
            if wert >= 100:
                wert = wert * 0.95
            total = total + wert
            anzahl = anzahl + 1
            name = b['kunde'].strip().lower().capitalize()
            zeilen.append(name + ': ' + b['artikel'] + ' = ' + str(round(wert, 2)) + ' CHF')
    kopf = 'Bestellungen (' + str(anzahl) + ')'
    strich = '-' * len(kopf)
    fuss = 'Total: ' + str(round(total, 2)) + ' CHF'
    return '\n'.join([kopf, strich] + zeilen + [strich, fuss])


if __name__ == '__main__':
    print(bericht(BESTELLUNGEN))
