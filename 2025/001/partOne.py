from input import *

instructions = data.strip().splitlines()

start = 50
counter = 0
for i in range(len(instructions)):
    parameter = 1 if instructions[i][0].lower() == "r" else -1

    start += int(instructions[i][1:])*parameter
    while start >= 100:
        start -= 100
    while start < 0:
        start +=100
    counter = counter+1 if start == 0 else counter

print(counter)  
