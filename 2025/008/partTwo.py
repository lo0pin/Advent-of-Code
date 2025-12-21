from input import data
import math

lines = data.splitlines()
circuits = []
#all_points_n_distances = []
distances_container = []
first = True

for i in range(len(lines)):    
    for j in range(i+1, len(lines)):
        first_point = lines[i].split(",")
        secon_point = lines[j].split(",")
        vector = []
        for k in range(3):
            vector.append(int(first_point[k])-int(secon_point[k]))
        distance = (pow(vector[0],2)+pow(vector[1],2)+pow(vector[2],2))
        distances_container.append([".".join(first_point),".".join(secon_point),distance])


distances_container.sort(key=lambda coord: coord[-1])
#print(distances_container[:1000])

#print("done")
#for i in distances_container[:1000]:
for i in distances_container:
    a = i[0]
    b = i[1]
    break_condition = False
    merge_counter = 0
    merge_indices = []


    for j in enumerate(circuits):

        #Both Points are already member of the same circuit --> Continue
        if a in j[1] and b in j[1]:
            break_condition = True
            break
        elif a in j[1]:
            merge_counter += 1
            merge_indices.append((j[0],b))
        elif b in j[1]:
            merge_counter += 1
            merge_indices.append((j[0],a))
        if merge_counter>=2:
            #break_condition = True
            break
    if break_condition:
        continue
    

    #besser mit match?
    if merge_counter >= 2:
        circuits[merge_indices[0][0]].extend(circuits[merge_indices[1][0]])
        del circuits[merge_indices[1][0]]
    elif merge_counter == 1:
        while merge_indices:   
            temp = merge_indices.pop(0)
            circuits[temp[0]].append(temp[1])
    elif merge_counter == 0:
        circuits.append([a, b])

    if len(circuits) == 1:
        if not first:
            result = int(a.split(".")[0]) * int(b.split(".")[0]) 
            print(result)
        first = False
        #print(int(a[0])*int(b[0]))
        


"""circuits.sort(reverse = True, key= lambda a : len(a))
result = 1"""

"""for i in range(3):
    result *= len(circuits[i])
    #print(len(circuits[i]))
    #print((circuits[i]))"""

"""print(len(circuits))

print(result)"""
