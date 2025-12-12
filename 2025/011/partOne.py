"""
NOT SOLVED
"""

from input import *

devices = data.splitlines()
device_outputs = [] #liste alle outputs
device_indices = [] #liste aller devices, um  mit indices zu arbeiten
complete_list  = []
for i in devices:
    device_outputs.append(i[5:].split(" "))
    device_indices.append(i.split(" ")[0][:3])

    complete_list.append(i.split(" "))
    complete_list[-1][0] = complete_list[-1][0][:3]
#print(complete_list[:10])

def get_index_from_string(kennung):
    if kennung in device_indices:
        return device_indices.index(kennung)
    return None
#print(get_index_from_string("rus"))

def get_outputs_from_string(kennung):
    if kennung in device_indices:
        return device_outputs[get_index_from_string(kennung)]  
#print(get_outputs_from_string("rus"))



def find_ahne(suchbegriff):
    lead_to_suchbegriff = []
    for i in range(len(device_outputs)):
        if suchbegriff in device_outputs[i]:
            #print(complete_list[i])
            lead_to_suchbegriff.append(device_indices[i])
    return lead_to_suchbegriff

print(find_ahne("vii"))


start = "out"
for counter in range(100):
    for i in find_ahne(start):
        print(i)
    start=i
    print()







"""print (device_outputs[:10])
print (device_indices[:10])"""


#print(device_list[:10])
############

#indices erstellen für schnelleren zugriff(alternativ: Dictionary)
#funktion zum abrufen des index für einen string
#@param: string
#@return: index
"""list_of_indices = []
for i in device_list:
    list_of_indices.append(i[0])

"""
############




