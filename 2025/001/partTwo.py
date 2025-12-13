from input import data

instructions = data.strip().splitlines()

start = 50
counter = 0
for i in range(len(instructions)):
    parameter = 1 if instructions[i][0].lower() == "r" else -1

    for j in range(0, int(instructions[i][1:])):
        start += 1*parameter
        match start:
            case -1:
                start=99
            case 100:
                start=0
        counter = counter+1 if start == 0 else counter 

print(counter)

