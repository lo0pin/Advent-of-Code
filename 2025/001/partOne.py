from "001input.py" import *

codes = [line.strip() for line in input.splitlines() if line.strip()]

# Startposition des Zahlendrehrads (laut Aufgabe beginnt es bei 50)
start = 50

# Zähler für die Anzahl der "Klicks", bei denen die Skala genau auf 0 steht
counter = 0

# Alle Rotationsanweisungen nacheinander abarbeiten
for code in codes:
    # Erstes Zeichen ist die Drehrichtung: 'L' (left) oder 'R' (right)
    direction = code[0]
    # Die restlichen Zeichen sind die Anzahl der Klicks als Zahl (egal ob 1, 2, 3 oder mehr Stellen)
    steps = int(code[1:])

    # Aus der Richtung ein Schritt-Vorzeichen machen:
    # links bedeutet -1 (Zahlen werden kleiner), rechts bedeutet +1 (Zahlen werden größer)
    if direction == 'L':
        step = -1
    elif direction == 'R':
        step = 1
    else:
        # Falls doch einmal ein ungültiger Buchstabe auftaucht, lieber hart abbrechen
        raise ValueError(f"Unbekannte Richtung in Code: {code}")

    # Jetzt wird die Rotation Klick für Klick simuliert
    for _ in range(steps):
        # Ein Klick weiterdrehen:
        # (start + step) bewegt den Zeiger, % 100 sorgt für das "Rundherum" von 0 bis 99
        # Beispiel: 99 + 1 = 100 -> 100 % 100 = 0
        #           0  - 1 = -1  -> -1 % 100 = 99
        start = (start + step) % 100

        # Nach jedem einzelnen Klick prüfen:
        # Zeigt der Zeiger jetzt genau auf 0? Dann haben wir einen relevanten "Treffer"
        if start == 0:
            counter += 1

# Am Ende ausgeben, wie oft während aller Klicks die 0 erreicht wurde
print(counter)
