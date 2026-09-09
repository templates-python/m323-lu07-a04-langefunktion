# LU07.A04 - Lösungshinweise

## Commit-Folge

```
refactor: Guard-Bedingung als ist_gueltig() extrahiert
refactor: Rabattgrenze und -satz als Konstanten benannt
refactor: Zeilenwert in zeilenwert() extrahiert
refactor: Namensaufbereitung in kundenname() extrahiert
refactor: Zeilenformatierung in zeile() extrahiert
refactor: Schleife durch Comprehension und sum() ersetzt
refactor: String-Verkettung durch f-Strings ersetzt
```

Nach jedem dieser Commits sind alle sechs Tests grün.

## Die Falle in dieser Aufgabe

Der naheliegende Umbau

```python
total = round(sum(zeilenwert(b) for b in gueltige), 2)
```

ist **falsch**. Bei einer leeren Liste liefert `sum()` den int `0`, das Original
arbeitet mit `total = 0.0` und liefert den float `0.0`. Der Bericht endet dann mit
`Total: 0 CHF` statt `Total: 0.0 CHF`. Richtig ist:

```python
total = round(sum((zeilenwert(b) for b in gueltige), 0.0), 2)
```

`test_leere_liste` deckt genau das auf. Ohne diesen Test wäre die Änderung
unbemerkt durchgegangen — und in einer Rechnungsansicht später als kosmetischer
Bug wieder aufgetaucht.

## Zweite Stolperstelle

Wer in `zeilenwert()` rundet statt erst beim Total, bekommt bei anderen
Datensätzen Rundungsdifferenzen im Total. Runden gehört an den Schluss.

## Bewertungshinweise

| Kriterium | Erfüllt, wenn |
|---|---|
| Zerlegung | mindestens drei Hilfsfunktionen mit fachlichen Namen |
| Konstanten | Rabattgrenze und Rabattsatz benannt |
| Pipeline | Schleife durch Comprehension und `sum()` ersetzt |
| Commits | ein Commit pro Technik, Technik in der Message genannt |
| Verhalten | alle sechs Tests grün, `main_test.py` unverändert |
