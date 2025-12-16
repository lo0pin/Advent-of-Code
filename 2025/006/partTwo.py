from input import data
from math import prod

correct_answer = 11708563470209

def debug(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}\t")
    print()

lines = data.splitlines()
math_operations = [d for d in lines[-1] if not d.isspace()]

#debug(math_operations=math_operations)

def get_indices():
    indices = []
    for i in range(len(lines[0])):
        num_count = 0
        for j in range(len(lines)-1):
            if lines[j][i].isnumeric():
                num_count += 1
        if num_count > 0:
            indices.append("#")
        else:
            indices.append(".")
    return indices
    
indices_counter = get_indices()

#debug(indices_counter=indices_counter)

result = 0
math_index = 0

numbers = []
for i in range(len(lines[0])):
    
    if indices_counter[i] == ".":
        if numbers:
            if math_operations[math_index]=="+":
                zwischenergebnis = sum(numbers)
            else:
                zwischenergebnis = prod(numbers)
            result += zwischenergebnis
            math_index += 1
        numbers = []
        continue
    else:
        number = ""

        for j in range(0,len(lines)-1):
            if lines[j][i].isnumeric():
                number+=lines[j][i]
        if number:
            numbers.append(int(number))

if numbers:
    if math_operations[math_index] == "+":
        result += sum(numbers)
    else:
        result += prod(numbers)

print(result)
print(result==correct_answer)
