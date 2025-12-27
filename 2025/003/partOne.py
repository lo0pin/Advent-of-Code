from input import data

list_of_lines = data.splitlines()

final_result = 0

for line in list_of_lines:
    zehner_max_value = 0
    einer_max_value  = 0
    idx = 0
    
    #zehnerstelle + index finden
    for j in enumerate(line):
        val = int(j[1])
        if val > zehner_max_value and j[0] <(len(line)-1):
            zehner_max_value = val
            idx = j[1]


    for k in range((idx+1),len(line)):
        if int(line[k]) > einer_max_value:
            einer_max_value = int(line[k])
    
    result = str(zehner_max_value)+str(einer_max_value)
    final_result += int(result)
    #print (f"{(list_of_lines.index(line)+1)}. {result}")

print (final_result)
