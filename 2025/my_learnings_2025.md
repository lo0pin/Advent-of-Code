````md
# Python-Konzepte – logisch sortiert mit Kurzbeschreibung & Beispiel

Diese Sammlung ordnet typische Python-“Bausteine” so, wie sie in echten Programmen oft gemeinsam auftreten:  
**Daten einlesen → aufbereiten → verarbeiten → Ergebnisse speichern → Laufzeit/Progress anzeigen.**

---

## 1) Textdaten in Zeilen zerlegen (`splitlines()`)

**Was ist das?**  
Wenn du einen großen Textblock (z. B. Dateiinhalt oder Input-String) hast, zerlegt `splitlines()` ihn in einzelne Zeilen. Das ist der Standard-Startpunkt fürs Parsen.

**Snippet**
```python
lines = data.splitlines()
````

**Beispiel**

```python
data = "a,b,c\n1,2,3\n4,5,6"
lines = data.splitlines()
print(lines)
# ['a,b,c', '1,2,3', '4,5,6']
```

---

## 2) Eine Zeile in Spalten zerlegen (`split(",")`)

**Was ist das?**
Mit `split(",")` teilst du eine Zeile in Teile (z. B. CSV-Spalten). Typisch: erst `splitlines()`, dann je Zeile `split()`.

**Snippet**

```python
lines[i].split(",")
```

**Beispiel**

```python
lines = ["a,b,c", "1,2,3"]
cols = lines[1].split(",")
print(cols)
# ['1', '2', '3']
```

---

## 3) Iterieren mit Index: `enumerate(...)`

**Was ist das?**
`enumerate(iterable)` liefert Paare aus `(index, element)`. Du bekommst den Index “gratis” und musst ihn nicht selbst mitzählen.

**Besser als**

* manuell `i += 1`
* oder `range(len(...))` (geht, ist aber oft unleserlicher)

**Snippet (korrigiert)**

```python
for j, circuit in enumerate(circuits):
    print(j, circuit)
```

**Beispiel**

```python
circuits = ["svr->dac", "svr->fft", "dac->out"]
for j, c in enumerate(circuits):
    print(f"{j}: {c}")
# 0: svr->dac
# 1: svr->fft
# 2: dac->out
```

---

## 4) Sortieren nach einem Kriterium: `list.sort(key=...)`

**Was ist das?**
Du sortierst eine Liste “nach” einem bestimmten Teil jedes Elements. Mit `key` sagst du: *“Woran soll die Reihenfolge festgemacht werden?”*

**Snippet**

```python
distances_container.sort(key=lambda coord: coord[-1])
```

**Was bedeutet `coord[-1]`?**
Das ist das **letzte Element** einer Sequenz (Liste/Tuple). Praktisch, wenn du z. B. `(x, y, dist)` speicherst und nach `dist` sortieren willst.

**Beispiel**

```python
distances_container = [
    (0, 0, 12.5),
    (5, 2, 3.1),
    (9, 9, 7.0),
]
distances_container.sort(key=lambda coord: coord[-1])
print(distances_container)
# [(5, 2, 3.1), (9, 9, 7.0), (0, 0, 12.5)]
```

---

## 5) Wertebereich prüfen: Vergleichskette `lower <= x <= upper`

**Was ist das?**
Python kann Vergleiche “ketten”. Das liest sich wie Mathe und ist exakt das: **liegt `y` zwischen zwei Grenzen?**

**Snippet**

```python
if lower_y <= y <= upper_y:
```

**Beispiel**

```python
lower_y, upper_y = 10, 20
for y in [5, 10, 15, 20, 25]:
    if lower_y <= y <= upper_y:
        print(y, "ist im Bereich")
# 10 ist im Bereich
# 15 ist im Bereich
# 20 ist im Bereich
```

---

## 6) Aus einer Liste “vorn” nehmen: `pop(0)` (Queue-Verhalten)

**Was ist das?**
`pop(0)` entfernt das **erste** Element und gibt es zurück. Das ist wie eine Warteschlange: *vorn rein/vorn raus*.

**Snippet**

```python
temp = merge_indices.pop(0)
```

**Beispiel**

```python
merge_indices = [10, 11, 12]
first = merge_indices.pop(0)
print(first)         # 10
print(merge_indices) # [11, 12]
```

**Achtung (ehrlich, ohne Zucker):**
`pop(0)` ist bei großen Listen langsam, weil alle Elemente nachrutschen müssen.
Für echte Queues nimm `collections.deque`.

```python
from collections import deque
q = deque([10, 11, 12])
first = q.popleft()
```

---

## 7) Laufzeit messen: `time.perf_counter()`

**Was ist das?**
`perf_counter()` ist eine hochauflösende Uhr zum Messen von Laufzeiten (Benchmarking). Du nimmst Startzeit, Endzeit, Differenz.

**Snippet**

```python
import time
t0 = time.perf_counter()
# ... Code ...
t1 = time.perf_counter()
print(f"Laufzeit: {t1 - t0:.6f} s")
```

**Beispiel**

```python
import time

t0 = time.perf_counter()
total = sum(i*i for i in range(1_000_00))
t1 = time.perf_counter()

print(f"Laufzeit: {t1 - t0:.6f} s, total={total}")
```

---

## 8) Dateien schreiben: `open(..., "w")` und `open(..., "a")`

### 8.1 Schreiben (neu erstellen/überschreiben): `"w"`

**Was ist das?**
`"w"` überschreibt die Datei komplett (oder erstellt sie neu).

**Snippet**

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(area_strings_for_export))
```

**Beispiel**

```python
lines = ["Zeile 1", "Zeile 2", "Zeile 3"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
```

### 8.2 Anhängen: `"a"` (append)

**Was ist das?**
`"a"` hängt an das Dateiende an, ohne vorhandenes zu löschen.

**Snippet**

```python
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Neue Zeile\n")
```

**Beispiel**

```python
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Noch eine Zeile\n")
```

---

## 9) List Comprehension (Listen elegant bauen)

**Was ist das?**
Eine kompakte Schreibweise, um aus einem Iterable eine neue Liste zu erzeugen — optional mit Filter.

### 9.1 Mapping: “jedes Element umformen”

```python
nums = [1, 2, 3]
doubles = [n * 2 for n in nums]
print(doubles)  # [2, 4, 6]
```

### 9.2 Filtern: “nur bestimmte Elemente behalten”

```python
nums = [1, 2, 3, 4, 5]
odds = [n for n in nums if n % 2 == 1]
print(odds)  # [1, 3, 5]
```

### 9.3 Strings bearbeiten

```python
names = ["julian", "alma", "matilda"]
caps = [name.capitalize() for name in names]
print(caps)  # ['Julian', 'Alma', 'Matilda']
```

### 9.4 Wörter nach Länge filtern

```python
words = ["boot", "stern", "sailing", "ki", "python"]
long = [w for w in words if len(w) >= 5]
print(long)  # ['stern', 'sailing', 'python']
```

### 9.5 Zeilen “säubern”: leere Zeilen und Kommentare raus

```python
lines = ["# comment", "data1", "", "data2", "   ", "data3"]
clean = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
print(clean)  # ['data1', 'data2', 'data3']
```

---

## 10) `if ... else` **in** Comprehensions (anderer Platz als Filter-`if`)

**Was ist das?**
Das ist **kein Filter**, sondern ein **Ausdruck**: *Wenn Bedingung, dann Wert A, sonst Wert B.*

**Merksatz**

* **Filter-`if`** steht **am Ende** (nach dem `for`)
* **if/else-Ausdruck** steht **vor** dem `for`

**Syntax**

```python
[ A if BEDINGUNG else B for ELEMENT in ITERABLE ]
```

**Beispiel: gerade Zahlen durch 0 ersetzen**

```python
nums = [1, 2, 3, 4, 5]
mapped = [n if n % 2 == 1 else 0 for n in nums]
print(mapped)  # [1, 0, 3, 0, 5]
```

**Beispiel: Wörter klassifizieren**

```python
words = ["a", "ab", "abc", "abcd"]
labels = ["kurz" if len(w) <= 2 else "lang" for w in words]
print(labels)  # ['kurz', 'kurz', 'lang', 'lang']
```

---

## 11) Fortschritt in einer Zeile anzeigen: `\r` + `flush=True`

**Was ist das?**
`\r` (Carriage Return) springt zum Zeilenanfang zurück.
Damit kannst du in der Konsole **dieselbe Zeile** immer wieder überschreiben (Progress-Anzeige).

**Snippet**

```python
print(f"\r{' ' * 40}", end="")         # alte Zeile wegwischen
print(f"\r{progress:.6f} %", end="", flush=True)
```

**Beispiel**

```python
import time

for i in range(101):
    progress = i
    print("\r" + " " * 30, end="")  # Zeile leeren
    print(f"\rFortschritt: {progress:3d} %", end="", flush=True)
    time.sleep(0.02)

print()  # am Ende Zeilenumbruch
```

---

## 12) `map()` – Funktion auf jedes Element anwenden

**Was ist das?**
`map(func, iterable)` ruft `func(x)` für jedes Element `x` auf.
Ergebnis ist ein **Iterator** (oft in `list(...)` umwandeln, wenn du’s sehen willst).

### 12.1 Ein Iterable: Länge jedes Strings

**Snippet**

```python
def myfunc(n):
    return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
```

**Beispiel**

```python
def myfunc(n):
    return len(n)

x = map(myfunc, ("apple", "banana", "cherry"))
print(list(x))  # [5, 6, 6]
```

### 12.2 Zwei Iterables: Elemente paarweise kombinieren

**Snippet**

```python
def myfunc(a, b):
    return a + b

x = map(myfunc,
        ('apple', 'banana', 'cherry'),
        ('orange', 'lemon', 'pineapple'))
```

**Beispiel**

```python
def myfunc(a, b):
    return a + " + " + b

x = map(myfunc,
        ("apple", "banana", "cherry"),
        ("orange", "lemon", "pineapple"))

print(list(x))
# ['apple + orange', 'banana + lemon', 'cherry + pineapple']
```

**Praxis-Tipp:**
Wenn du ohnehin schon List Comprehensions nutzt, ist das oft lesbarer als `map()`:

```python
lengths = [len(s) for s in ("apple", "banana", "cherry")]
```

---

## Mini-Flow-Beispiel (alles in einem realistischen Ablauf)

Hier ein kleines “so läuft’s in echt”-Szenario: Textdaten → parsen → filtern → sortieren → speichern → Laufzeit anzeigen.

```python
import time

data = "x,y,dist\n0,0,12.5\n5,2,3.1\n9,9,7.0\n# comment\n\n"

t0 = time.perf_counter()

lines = data.splitlines()
clean = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]

header, *rows = clean
distances = []
for i, row in enumerate(rows):
    x, y, d = row.split(",")
    distances.append((int(x), int(y), float(d)))

distances.sort(key=lambda coord: coord[-1])

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(str(t) for t in distances))

t1 = time.perf_counter()
print(f"Laufzeit: {t1 - t0:.6f} s")
```

---

```

Wenn du willst, kann ich dir daraus auch eine hübsche Repo-Struktur machen (z. B. `snippets/README.md` + einzelne `*.py`-Beispieldateien), aber das hier ist bereits “copy & paste” GitHub-ready.
```
