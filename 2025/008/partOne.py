from input import *
import math

lines = data.splitlines()
#mittelwert_distance =0
#counter_distance = 0
shortest_distance = 99999999999999999999
idx_shortest_dist = 0
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
        distance = math.sqrt(pow(vector[0],2)+pow(vector[1],2)+pow(vector[2],2))
        distances_container.append([".".join(first_point),".".join(secon_point),distance])



short_list = []
current_shortest = 0


HOW_MANY_VALUES = 1000

#for j in range(len(distances_container)-1):
for j in range(HOW_MANY_VALUES):
    shortest_distance = 99999999999999999999  
    ############################
    #Progress counter
    if j % (HOW_MANY_VALUES/10) == 0:
        print (j/HOW_MANY_VALUES*100, " %")
    ############################
    for i in range(len(distances_container)):
        if distances_container[i][2]< shortest_distance and distances_container[i][2]>current_shortest:
            shortest_distance = distances_container[i][2]
            idx_shortest_dist = i


    current_shortest = shortest_distance

    short_list.append(idx_shortest_dist)

break_condition = False
merge_counter = 0
merge_condition = False

for i in short_list:
    for j in circuits:
        break_condition = False
        if distances_container[i][0] in j and distances_container[i][1] in j:
            """print("2 punkte in einem circiut")
            print(distances_container[i][0], " and ", distances_container[i][1], " already in: ", j)"""
            break_condition = True
            break
    if break_condition:
        #print("break_condition")
        break_condition = False
        continue
    break_condition = False

    idx_ciricuits=[]
    merge_counter = 0
    for j in range(len(circuits)):
        if distances_container[i][0] in circuits[j] or distances_container[i][1] in circuits[j]:
            merge_counter += 1
            idx_ciricuits.append(j)
    if merge_counter >=2:
        #print("merge_condition")
        merged_circuit = []
        for m in idx_ciricuits:
            for n in range(len(circuits[m])):
                merged_circuit.append(circuits[m][n])
            circuits.remove(circuits[m])
        circuits.append(merged_circuit)
        #merged_circuit.clear()
        merge_counter = 0
        continue
    

    for j in circuits:
        if distances_container[i][0] in j:
            j.append(distances_container[i][1])
        elif distances_container[i][1] in j:
            j.append(distances_container[i][0])
    if merge_counter == 0:
        new_circuit = [distances_container[i][0], distances_container[i][1]]
        circuits.append(new_circuit)


"""print(circuits)
print(len(circuits))"""
lengths = []
for i in circuits:
    #print(len(i), end=", ")
    lengths.append(len(i))

lengths.sort(reverse=True)
#print (lengths)

result= lengths[0]*lengths[1]*lengths[2]
print(result)



"""print(short_list)
print(len(distances_container))
print()
print(distances_container[short_list[0]][2])
print(distances_container[short_list[1]][2])
print(distances_container[short_list[2]][2])
"""




