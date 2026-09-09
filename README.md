# LU07.A04 - Lange Funktion zerlegen

Modul 323, LU07 Refactoring · Kompetenzfeld **D1I**

Die Funktion `bericht` in `main.py` funktioniert korrekt. Sie filtert, rechnet,
formatiert und baut die Ausgabe in einem einzigen Block. Ihre Aufgabe ist es,
die Funktion lesbar zu machen — **ohne die Ausgabe zu verändern**.

## Auftrag

1. Führen Sie `pytest` aus. Alle Tests sind grün. Das ist Ihr Sicherheitsnetz.
2. Wenden Sie mindestens vier Techniken aus
   [LU07c](https://wiki.bzz.ch/modul/m323/learningunits/lu07/techniken) an.
   Erwartet werden: Extract Function, Replace Magic Number with Named Constant,
   Replace Loop with Pipeline, sprechende Namen.
3. **Ein Refactoring, ein Commit.** Die Commit-Message nennt die Technik, zum Beispiel
   `refactor: Rabattgrenze als Konstante benannt`.
4. Nach jedem Commit: `pytest` laufen lassen. Rot heisst zurück zum letzten grünen Stand.
5. Am Schluss soll keine Funktion länger als etwa zehn Zeilen sein.

## Regeln

* `main_test.py` wird **nicht** verändert. Wer den Test anpasst, damit er grün wird,
  hat die Aufgabe nicht gelöst.
* Die Namen `BESTELLUNGEN` und `bericht` bleiben erhalten — nur so laufen die Tests.
* Neue Hilfsfunktionen dürfen Sie frei benennen.

## Bewertung

| Teil | Punkte |
|---|---|
| Tests (`main_test.py`) | 8 |
| pylint (`main.py`) | 5 |

Die Tests prüfen, dass sich das Verhalten nicht verändert hat. Die Lint-Punkte
prüfen, ob der Code danach den Konventionen entspricht.

## Lokal prüfen

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest
python _run_pylint.py
```

## Achtung

Die Beispieldaten sind nicht der einzige Testfall. Denken Sie an die leere Liste
und an die Rabattgrenze bei genau 100 Franken — dort passieren beim Umbau die
meisten stillen Verhaltensänderungen.
