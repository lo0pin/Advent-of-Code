"""
NOT SOLVED
"""

from input import *

#liste erstellen
#liste aus listen von strings; 0. elment = devicename, alle anderen = output
devices = data.splitlines()
device_list = []
for i in devices:
    device_list.append(i.split(" "))
    device_list[-1][0] = device_list[-1][0][:3]

#print(device_list[:10])
############

#indices erstellen für schnelleren zugriff(alternativ: Dictionary)
#funktion zum abrufen des index für einen string
#@param: string
#@return: index
list_of_indices = []
for i in device_list:
    list_of_indices.append(i[0])

def getindex(kennung):
    if kennung in list_of_indices:
        return list_of_indices.index(kennung)
    return None
############

def check_path(inp):
    for i in range(len(device_list)):

        if xy[-1] == "out":
            return True

    return False

############

"""
Vorgangsweise:
1) alle OUT indentifizieren
2) wege vom OUT zurückverfolgen
"""

"""for device in range(1, len(device_list[getindex("you")])):
    while
"""


"""list_of_exits = []
for i in device_list:
    if i[-1] == "out":
        list_of_exits.append(i[0])
        
list_of_exits.sort()
print(list_of_exits)"""

def take_step(current_index):









