from input import data

lines = data.splitlines()
lines = lines[2:-1:2]
print(len(lines))

paths = []
for i in range(len(lines[0])):
    paths.append(0)
paths[70]=1

for line in range(len(lines)):
    to_add = []
    for idx in range(len(lines[line])):
        if lines[line][idx] == "^" and paths[idx] > 0:
            to_add.append((idx,paths[idx]))
        elif paths[idx] > 0:
            paths[idx] 

    for i in to_add:
        paths[i[0]] = 0
        paths[i[0]-1] += i[1]
        paths[i[0]+1] += i[1]
    
#print(paths)
print(sum(paths))
