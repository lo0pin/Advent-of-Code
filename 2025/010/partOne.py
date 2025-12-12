from input import *

instructions = data.splitlines()
instructions_per_machine = []

"""for  machine in instructions:
    instructions_per_machine.append(machine.split(" "))"""



def apply_button(state_string, button_list):
    state_list = list(state_string)

    for i in button_list:
        if state_list[i] == ".":
            state_list[i] = "#"
        else:
            state_list[i] = "." 
    return "".join(state_list)

def minimum_button_presses(zielstring, buttons):
    start = "."*len(zielstring)

    queue = []
    queue.append((start, 0))

    visited = set()
    visited.add(start)

    while queue:
        state, dist = queue.pop(0)
        if state == zielstring:
            return dist
        
        for button in buttons:
            new_state = apply_button(state, button)
            if  new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, dist+1))
    return None


for  machine in instructions:
    buffer = []
    for i in machine.split(" "):
        if "[" in i:
            buffer.append(i.strip("[]"))   
        elif "(" in i:
            buffer.append(i.strip("()"))
        #für diese Aufgabe irrelavant
        """elif "{" in i:
            buffer.append(i.strip("{}"))"""
    instructions_per_machine.append(buffer)

machines = []  # Liste von (ziel_string, buttons)

for parts in instructions_per_machine:
    ziel_string = parts[0]
    button_strings = parts[1:]

    buttons = []
    for b in button_strings:
        indices = []
        if b != "":  # falls mal was Leeres reinkommt
            for idx in b.split(","):
                indices.append(int(idx))
        buttons.append(indices)

    machines.append((ziel_string, buttons))

print(machines[:5])

button_total = 0

for ziel_string_, buttons in machines:
    presses = minimum_button_presses(ziel_string_, buttons)
    button_total += presses

print(button_total)


