"""
Lösung für das Rätsel mit den „ungültigen“ Produkt-IDs.

Regel:
Eine ID ist *ungültig*, wenn sie aus einer Ziffernfolge besteht, die exakt zweimal
direkt hintereinander steht, z.B.:
    11      -> "1" + "1"
    6464    -> "64" + "64"
    123123  -> "123" + "123"

Wichtig:
- Die Zahl darf keine führende Null haben (passiert bei int → str automatisch nicht).
- Die Gesamtlänge der Ziffern muss gerade sein (sonst kann man sie nicht in zwei
  gleich lange Hälften teilen).
"""

# Unsere Eingabe: alle ID-Bereiche in einer einzigen Zeichenkette
RANGE_INPUT = (
    "26803-38596,161-351,37-56,9945663-10044587,350019-413817,"
    "5252508299-5252534634,38145069-38162596,1747127-1881019,609816-640411,"
    "207466-230638,18904-25781,131637-190261,438347308-438525264,"
    "5124157617-5124298820,68670991-68710448,8282798062-8282867198,"
    "2942-5251,659813-676399,57-99,5857600742-5857691960,9898925025-9899040061,"
    "745821-835116,2056-2782,686588904-686792094,5487438-5622255,325224-347154,"
    "352-630,244657-315699,459409-500499,639-918,78943-106934,3260856-3442902,"
    "3-20,887467-1022885,975-1863,5897-13354,43667065-43786338"
)


def is_invalid_id(n: int) -> bool:
    """
    Prüft, ob eine gegebene Zahl `n` eine „ungültige“ ID ist.

    Kriterien:
    - Schreibe `n` als Dezimalstring s = str(n).
    - Wenn die Länge von s ungerade ist → keine Dopplung möglich → False.
    - Teile s in zwei gleich lange Hälften:
        left = s[:len(s)//2]
        right = s[len(s)//2:]
      Wenn left == right, dann ist s eine exakte Wiederholung.
    """
    s = str(n)

    # Ungerade Länge → keine Wiederholung möglich
    if len(s) % 2 == 1:
        return False

    half = len(s) // 2
    left = s[:half]
    right = s[half:]

    return left == right


def sum_invalid_ids_in_ranges(range_string: str) -> int:
    """
    Nimmt eine Zeichenkette mit Bereichen im Format:
        "start1-end1,start2-end2,..."
    und berechnet die Summe aller ungültigen IDs innerhalb dieser Bereiche.
    """
    total_sum = 0

    # Bereiche am Komma trennen
    for part in range_string.split(','):
        part = part.strip()
        if not part:
            continue

        # Ein Bereich: "start-end"
        start_str, end_str = part.split('-')
        start_id = int(start_str)
        end_id = int(end_str)

        # IDs durchlaufen
        for product_id in range(start_id, end_id + 1):
            if is_invalid_id(product_id):
                total_sum += product_id

    return total_sum


def main():
    """Startet die Berechnung und gibt das Ergebnis aus."""
    result = sum_invalid_ids_in_ranges(RANGE_INPUT)
    print("Summe aller ungültigen IDs:", result)


if __name__ == "__main__":
    main()
    # Hinweis: Ergebnis für die gesamte Eingabe ist:
    # 22062284697
