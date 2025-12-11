from input import *

ids = data.splitlines()

starts_and_ends = []
for id in ids:
    start = int(id.split("-")[0])
    end = int(id.split("-")[1])
    starts_and_ends.append([start, end])

def delete_completely_wrapped():
    counter = 0
    indices_to_delete_bc_wrapped = []
    for i in range(len(starts_and_ends)):
        for j in range(i+1, len(starts_and_ends)):
            if starts_and_ends[i][0] >= starts_and_ends[j][0] and starts_and_ends[i][1] <= starts_and_ends[j][1]:
                indices_to_delete_bc_wrapped.append(i)

    indices_to_delete_bc_wrapped.reverse()
    if len(indices_to_delete_bc_wrapped)>0:
        for i in indices_to_delete_bc_wrapped:
            if 0 <= i < len(starts_and_ends):   
                del starts_and_ends[i]
                counter +=1

    return(counter)

def handle_partially_wrapped():
    counter = 0
    indices_partially_wrapped = []    

    for i in range(len(starts_and_ends)):
        for j in range(i+1, len(starts_and_ends)):
            if (starts_and_ends[i][0] >= starts_and_ends[j][0] and starts_and_ends[i][0] < starts_and_ends[j][1]) or (starts_and_ends[i][1] <= starts_and_ends[j][1] and starts_and_ends[i][1] > starts_and_ends[j][0]):
                indices_partially_wrapped.append([i, j])

    indices_to_delete_bc_part_wrapped = []

    for i in indices_partially_wrapped:
        for j in i:
            if j not in indices_to_delete_bc_part_wrapped:
                indices_to_delete_bc_part_wrapped.append(j)

    ranges_to_add=[]

    for i in indices_partially_wrapped:
        #case = 0
        if (starts_and_ends[i[0]][0] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1)) or (starts_and_ends[i[1]][1] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1)):
            ranges_to_add.append([starts_and_ends[i[1]][0],starts_and_ends[i[0]][1]])
            #case = 14
        elif (starts_and_ends[i[0]][1] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1)) or (starts_and_ends[i[1]][0] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1)):
            ranges_to_add.append([starts_and_ends[i[0]][0],starts_and_ends[i[1]][1]])

    indices_to_delete_bc_part_wrapped.sort()
    indices_to_delete_bc_part_wrapped.reverse()

    for i in indices_to_delete_bc_part_wrapped:
        del starts_and_ends[i]
        counter +=1

    for i in ranges_to_add:
        starts_and_ends.append(i)
        counter +=1

    return (counter)








while(1):
    if delete_completely_wrapped() + handle_partially_wrapped() == 0:
        break

print("broken")
#print(indices_to_delete_bc_wrapped)
#print(indices_partially_wrapped)

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



        #case= 23

#print (ranges_to_add)
"""print(case)   
print(starts_and_ends[i[0]][0], end="\t")
print(starts_and_ends[i[0]][1], end="\t")
print(starts_and_ends[i[1]][0], end="\t")
print(starts_and_ends[i[1]][1], end="\n")"""



final_result = 0
for i in starts_and_ends:
    final_result += ((i[1]-i[0])+1)

print(final_result)


    

