from input import *
import math

lines = data.splitlines()


for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        first_point = lines[i].split(",")
        secon_point = lines[j].split(",")
        vector = []
        for k in range(3):
            vector.append(int(first_point[k])-int(secon_point[k]))
        distance = math.sqrt(pow(vector[0],2)+pow(vector[1],2)+pow(vector[2],2))
    print (vector)
    print (distance)
