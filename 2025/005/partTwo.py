from input import *

ids = data.splitlines()


freshies = []

starts_and_ends = []

for id in ids:
    start = int(id.split("-")[0])
    end = int(id.split("-")[1])
    starts_and_ends.append([start, end])

indices_to_delete_bc_wrapped = []
indices_partially_wrapped = []


for i in range(len(starts_and_ends)):
    for j in range(i+1, len(starts_and_ends)):
        if starts_and_ends[i][0] >= starts_and_ends[j][0] and starts_and_ends[i][1] <= starts_and_ends[j][1]:
            indices_to_delete_bc_wrapped.append(i)

indices_to_delete_bc_wrapped.reverse()
for i in indices_to_delete_bc_wrapped:
    del starts_and_ends[i]

for i in range(len(starts_and_ends)):
    for j in range(i+1, len(starts_and_ends)):
        if (starts_and_ends[i][0] >= starts_and_ends[j][0] and starts_and_ends[i][0] < starts_and_ends[j][1]) or (starts_and_ends[i][1] <= starts_and_ends[j][1] and starts_and_ends[i][1] > starts_and_ends[j][0]):
            indices_partially_wrapped.append([i, j])

#print(indices_to_delete_bc_wrapped)
#print(indices_partially_wrapped)
indices_to_delete_bc_part_wrapped = []

for i in indices_partially_wrapped:
    for j in i:
        if j not in indices_to_delete_bc_part_wrapped:
            indices_to_delete_bc_part_wrapped.append(j)

indices_to_delete_bc_part_wrapped.sort()
indices_to_delete_bc_part_wrapped.reverse()
#print(indices_to_delete_bc_part_wrapped)


"""for i in indices_partially_wrapped:
    case = 0
    if starts_and_ends[i[0]][0] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1):
        case = 1
    elif starts_and_ends[i[0]][1] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1):
        case = 2 
    elif starts_and_ends[i[1]][0] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1):
        case = 3
    elif starts_and_ends[i[1]][1] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1):
        case = 4
    print(case)"""


ranges_to_add=[]

for i in indices_partially_wrapped:
    #case = 0
    if (starts_and_ends[i[0]][0] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1)) or (starts_and_ends[i[1]][1] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1)):
        ranges_to_add.append([starts_and_ends[i[1]][0],starts_and_ends[i[0]][1]])
        #case = 14
    elif (starts_and_ends[i[0]][1] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1)) or (starts_and_ends[i[1]][0] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1)):
        ranges_to_add.append([starts_and_ends[i[0]][0],starts_and_ends[i[1]][1]])
        #case= 23

#print (ranges_to_add)
"""print(case)   
print(starts_and_ends[i[0]][0], end="\t")
print(starts_and_ends[i[0]][1], end="\t")
print(starts_and_ends[i[1]][0], end="\t")
print(starts_and_ends[i[1]][1], end="\n")"""

for i in indices_to_delete_bc_part_wrapped:
    del starts_and_ends[i]


for i in ranges_to_add:
    starts_and_ends.append(i)

final_result = 0
for i in starts_and_ends:
    final_result += ((i[1]-i[0])+1)

print(final_result)


    

    


"""print(starts_and_ends)
print("#################")
print(freshies)"""
