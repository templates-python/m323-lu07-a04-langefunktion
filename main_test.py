"""LU07.A04 - Sicherheitsnetz.

Diese Tests halten das heutige Verhalten von `bericht` fest.
Sie sind vor Ihrem ersten Umbau gruen und muessen es nach jedem
einzelnen Refactoring-Schritt bleiben.

Aendern Sie diese Datei nicht.
"""

import main

ERWARTET = (
    'Bestellungen (4)\n'
    '----------------\n'
    'Meier: Maus = 75.0 CHF\n'
    'Keller: Laptop = 1140.0 CHF\n'
    'Meier: Tastatur = 152.0 CHF\n'
    'Keller: Monitor = 199.5 CHF\n'
    '----------------\n'
    'Total: 1566.5 CHF'
)


def _bestellung(preis, status='offen', kunde='x', menge=1):
    """Baut eine einzelne Bestellung fuer die Testfaelle."""
    return {'kunde': kunde, 'artikel': 'a', 'menge': menge, 'preis': preis, 'status': status}


def test_bericht_unveraendert():
    """Der Bericht der Beispieldaten bleibt zeichengenau gleich."""
    assert main.bericht(main.BESTELLUNGEN) == ERWARTET


def test_stornierte_werden_ignoriert():
    """Stornierte Bestellungen zaehlen weder in der Anzahl noch im Total."""
    nur_storno = [_bestellung(60.0, status='storniert')]
    assert main.bericht(nur_storno) == (
        'Bestellungen (0)\n'
        '----------------\n'
        '----------------\n'
        'Total: 0.0 CHF'
    )


def test_rabatt_erst_ab_100():
    """Bei 99.00 gibt es keinen Rabatt."""
    assert 'a = 99.0 CHF' in main.bericht([_bestellung(99.0)])


def test_rabatt_ab_100_inklusive():
    """Bei genau 100.00 greifen die 5 Prozent Rabatt."""
    assert 'a = 95.0 CHF' in main.bericht([_bestellung(100.0)])


def test_kundenname_wird_normalisiert():
    """Fuehrende Leerzeichen und Grossschreibung werden vereinheitlicht."""
    assert 'Anna: a = 20.0 CHF' in main.bericht([_bestellung(20.0, kunde='  ANNA ')])


def test_leere_liste():
    """Ohne Bestellungen bleibt der Rahmen des Berichts erhalten."""
    assert main.bericht([]) == (
        'Bestellungen (0)\n'
        '----------------\n'
        '----------------\n'
        'Total: 0.0 CHF'
    )
