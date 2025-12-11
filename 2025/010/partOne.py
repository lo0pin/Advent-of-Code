from input import *

instructions = data.splitlines()
instructions_per_machine = []

"""for  machine in instructions:
    instructions_per_machine.append(machine.split(" "))"""

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

def apply_button(state_string, button_list):
    state_list = list(state_string)

    for i in button_list:
        if state_list[i] == ".":
            state_list[i] = "#"
        else:
            state_list[i] = "." 
    return "".join(state_list)
