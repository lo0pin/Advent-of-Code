#########DATENAUFBEREITUNG#########
from input import data

devices = data.splitlines()
mydic = {}

for i in devices:
    left = i[0:i.index(":")]
    right = i[i.index(":")+2:].strip().split(" ")
    mydic[left]=right


###########DATENAUFBEREITUNG############
alle_wege = []
start, ziel = "you", "out"
stack = [(start, (start,))]

##################CODE##################
while(stack):
    current, path = stack.pop()

    if current == ziel:
        alle_wege.append(path)
        continue

    for nxt in mydic.get(current, []):
        if nxt in path:
            continue

        stack.append((nxt, path+ (nxt,)))

################AUSGABE#################
print(len(alle_wege))
print(len(alle_wege) == len(set(alle_wege)))
