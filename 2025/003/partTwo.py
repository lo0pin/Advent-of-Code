from input import *

list_of_lines = data.splitlines()
#print(len(list_of_lines)) # 200 list_of_lines
# 100 numbers per line

final_result = 0

for line in list_of_lines: #über jede Zeile itierieren
    integers = []
    indices = []

    for j in range(11,-1,-1):
        try:
            start = indices[-1]
        except:
            start = 0
        current_maximum = 0
        #print(start)
        for i in range((start),len(line)):
            #print (current_maximum)
            if int(line[i]) > current_maximum and i < len(line)-j:
                current_maximum = int(line[i])
                current_max_idx = i 
        integers.append(str(current_maximum))
        indices.append(current_max_idx+1)


    result = "".join(integers)
    final_result += int(result)
    print(result)
    print(indices)

  

print (final_result)




