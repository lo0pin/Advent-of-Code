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

print(indices_to_delete_bc_wrapped)
print(indices_partially_wrapped)


for i in indices_partially_wrapped:
    case = 0
    if starts_and_ends[i[0]][0] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1):
        case = 1
    if starts_and_ends[i[0]][1] in range(starts_and_ends[i[1]][0],starts_and_ends[i[1]][1]+1):
        case = 2 
    if starts_and_ends[i[1]][0] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1):
        case = 3
    if starts_and_ends[i[1]][1] in range(starts_and_ends[i[0]][0],starts_and_ends[i[0]][1]+1):
        case = 4
    print(case)
    """print(starts_and_ends[i[0]][0], end="\t")
    print(starts_and_ends[i[0]][1], end="\t")
    print(starts_and_ends[i[1]][0], end="\t")
    print(starts_and_ends[i[1]][1], end="\n")"""
    
    """
     _____                    _____                    _____          
     /\    \                  /\    \                  /\    \         
    /::\    \                /::\    \                /::\    \        
    \:::\    \              /::::\    \              /::::\    \       
     \:::\    \            /::::::\    \            /::::::\    \      
      \:::\    \          /:::/\:::\    \          /:::/\:::\    \     
       \:::\    \        /:::/__\:::\    \        /:::/  \:::\    \    
       /::::\    \      /::::\   \:::\    \      /:::/    \:::\    \   
      /::::::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \  
     /:::/\:::\    \  /:::/\:::\   \:::\ ___\  /:::/    /   \:::\ ___\ 
    /:::/  \:::\____\/:::/__\:::\   \:::|    |/:::/____/     \:::|    |
   /:::/    \::/    /\:::\   \:::\  /:::|____|\:::\    \     /:::|____|
  /:::/    / \/____/  \:::\   \:::\/:::/    /  \:::\    \   /:::/    / 
 /:::/    /            \:::\   \::::::/    /    \:::\    \ /:::/    /  
/:::/    /              \:::\   \::::/    /      \:::\    /:::/    /   
\::/    /                \:::\  /:::/    /        \:::\  /:::/    /    
 \/____/                  \:::\/:::/    /          \:::\/:::/    /     
                           \::::::/    /            \::::::/    /      
                            \::::/    /              \::::/    /       
                             \::/____/                \::/____/        
                              ~~                       ~~              
    """
    


"""print(starts_and_ends)
print("#################")
print(freshies)"""
