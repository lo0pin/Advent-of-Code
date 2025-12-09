from input import *
import math

lines = data.splitlines()
mittelwert_distance =0
counter_distance = 0
shortest_distance = 99999999999999999999
idx_shortest_dist = 0
circuits = []
all_points_n_distances = []
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
for j in range(len(distances_container)-1):
    shortest_distance = 99999999999999999999  

    for i in range(len(distances_container)):
        if distances_container[i][2]< shortest_distance and distances_container[i][2]>current_shortest:
            shortest_distance = distances_container[i][2]
            idx_shortest_dist = i


    current_shortest = shortest_distance

    short_list.append(idx_shortest_dist)

#print(short_list)
print(distances_container[short_list[0]][2])
print(distances_container[short_list[1]][2])
print(distances_container[short_list[2]][2])





