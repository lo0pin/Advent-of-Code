from input import data

ranges = data.split(",")
solution = 0

for i in ranges:
    start_str, end_str = i.split("-")
    start_int, end_int = int(start_str), int(end_str)

    if len(start_str)%2==0 or len(end_str)%2==0:
        for j in range(start_int, end_int+1):
            j_str = str(j)
            if len(j_str)%2==1:
                continue
            cur_len_half = int(len(j_str)/2)
            if j_str[:cur_len_half] == j_str[cur_len_half:]:
                solution += j

print (solution)
