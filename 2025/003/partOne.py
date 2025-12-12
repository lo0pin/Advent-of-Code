from input import *

list_of_lines = data.splitlines()
#print(len(list_of_lines)) # 200 list_of_lines
# 100 numbers per line

final_result = 0

for line in list_of_lines:
    zehner_max_value = 0
    zehner_max_index = 0
    #zehnerstelle + index finden
    for j in range(len(line)):
        if int(line[j]) > zehner_max_value and j<(len(line)-1):
            zehner_max_value = int(line[j])
            zehner_max_index = j
    """
    print(zehner_max_value)
    print(zehner_max_index)
    print()    
    """
    einer_max_value = 0
    einer_max_index = 0
    for k in range((zehner_max_index+1),len(line)):
        if int(line[k]) > einer_max_value:
            einer_max_value = int(line[k])
    
    result = str(zehner_max_value)+str(einer_max_value)
    final_result += int(result)
    #print (f"{(list_of_lines.index(line)+1)}. {result}")

print (final_result)
