from input import data

machines = data.splitlines()
machineDic = {}

for i in machines: 
    left = i[0:i.index(":")]
    right = i[i.index(":")+2:].strip().split(" ")
    machineDic[left] = right

alle_wege = []
start, ziel = "svr", "out"
stack = [(start, (start,))]

"""print("go")
jey = 0"""

while stack:
    current, path = stack.pop()
    """print(f"\r{' ' * 40}", end="")         # alte Zeile wegwischen
    print(f"\r{len(stack)}\t\t{jey}", end="", flush=True)
    jey +=1"""

    if current == ziel:
        if "dac" in path and "fft" in path:
            alle_wege.append(path)
            continue

    for nxt in machineDic.get(current, []):
        if nxt in path:
            continue
        stack.append((nxt, path+ (nxt,)))
    
print(len(alle_wege))
