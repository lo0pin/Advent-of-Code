distances_container.sort(key=lambda coord: coord[-1])


lines = data.splitlines()
lines[i].split(",")

for j in enumerate(circuits):
  print(f"j[0]. j[1]")

temp = merge_indices.pop(0)

if lower_y <= y <= upper_y:

import time
t0 = time.perf_counter()
t1 = time.perf_counter()
print(f"Laufzeit: {t1 - t0:.6f} s")


with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(area_strings_for_export))

with open("output.txt", "a", encoding="utf-8") as f: #"a" = append
    f.write("Neue Zeile\n") 

## **list comprehension**
nums = [1, 2, 3]
doubles = [n * 2 for n in nums]
-> [2, 4, 6]

### Beispiel C: Strings bearbeiten
names = ["julian", "alma", "matilda"]
caps = [name.capitalize() for name in names]
-> ["Julian", "Alma", "Matilda"]

### Beispiel A: ungerade Zahlen
odds = [n for n in nums if n % 2 == 1]

### Beispiel B: Wörter nach Länge filtern
words = ["boot", "stern", "sailing", "ki", "python"]
long = [w for w in words if len(w) >= 5]
-> ["stern", "sailing", "python"]

### Beispiel C: Zeilen aus Datei / Text filtern
lines = ["# comment", "data1", "", "data2", "   ", "data3"]
clean = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
-> ["data1", "data2", "data3"]

### 3) if ... else in Comprehensions (anderer Platz!)
[ AUSDRUCK_IF_TRUE if BEDINGUNG else AUSDRUCK_IF_FALSE for ELEMENT in ITERABLE ]
Beim Filter-if steht if am Ende (nach dem for)

Beim if/else-Ausdruck steht if/else vor dem for

nums = [1, 2, 3, 4, 5]
mapped = [n if n % 2 == 1 else 0 for n in nums]
-> [1, 0, 3, 0, 5]

words = ["a", "ab", "abc", "abcd"]
-> ["kurz", "kurz", "lang", "lang"]


print(f"\r{' ' * 40}", end="")         # alte Zeile wegwischen
print(f"\r{progress:.6f} %", end="", flush=True)