from input import *

ids = data.splitlines()

starts_and_ends = []
for id in ids:
    start = int(id.split("-")[0])
    end = int(id.split("-")[1])
    starts_and_ends.append([start, end])

starts_and_ends.sort(key=lambda pair: pair[0])

merged = []

for current in starts_and_ends:
    current_start = current[0]
    current_end = current[1]

    
    if len(merged) == 0:
        merged.append([current_start, current_end])
    else:
        
        last_start = merged[-1][0]
        last_end = merged[-1][1]

        if current_start <= last_end:
            if current_end > last_end:
                merged[-1][1] = current_end
        else:
            merged.append([current_start, current_end])

final_result = 0
for interval in merged:
    start = interval[0]
    end = interval[1]

    final_result += (end - start + 1)

print(final_result)
