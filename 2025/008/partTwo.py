from input import data
import math

lines = data.splitlines()
circuits = []
#all_points_n_distances = []
distances_container = []

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
#print(distances_container[:100])

print("done")
for i in distances_container:
    a = distances_container[i][0]
    b = distances_container[i][1]
    break_condition = False
    merge_counter = 0
    merge_indices = []

    for j in enumerate(circuits):

        #Both Points are member of the same circuit --> Continue
        if a in j[1] and b in j[1]:
            break_condition = True
            break
        elif a in j[1] or b in j[1]:
            merge_counter += 1
            merge_indices.append(j[0])
    if break_condition:
        continue




