from input import *

ids = data.splitlines()

foods = data2.splitlines()
fresh_counter = 0

for food in foods:
    food = int(food)
    for id in ids:
        start = int(id.split("-")[0])
        end = int(id.split("-")[1])
        if food >= start and food <= end:
            fresh_counter += 1
            break
        else:
            continue
        


print (fresh_counter)
