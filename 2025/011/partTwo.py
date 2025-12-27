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

