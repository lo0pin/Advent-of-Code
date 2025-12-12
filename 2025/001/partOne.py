from input import *

instructions = data.strip().splitlines()
#print(instructions)

directions = []
moves = []
for i in instructions:
    directions.append(i[0])
    moves.append(int(i[1:]))
#print (moves)

start = 50
counter = 0
for i in range(len(instructions)):
    if directions[i].lower() == "r":
        start+=moves[i]
    else:
        start-=moves[i]

    while start>= 100:
        start-=100
    while start < 0:
        start += 100

    if start == 0:
        counter +=1

print(counter)
