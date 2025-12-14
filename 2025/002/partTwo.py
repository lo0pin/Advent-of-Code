"""
Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), 
and 1111111 (1 seven times) are all invalid IDs.
"""

def debug(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}\t")
    print()

from input import data

ranges = data.split(",")
solution = 0
correct_solution = 46666175279

"""
returns the divisors of a given number
@param: integer num
@return: list of integers that devide num w/o rest"""
def get_divisors(num):
    return [d for d in range(1,num) if num % d == 0]


for i in ranges:
    start_str, end_str = i.split("-")
    start_int, end_int = int(start_str), int(end_str)

    for j in range(start_int, end_int+1): #alle Zahlen iterieren
        j_str = str(j)

        #debug(j_str=j_str, len_j_str=len(j_str),get_divisors_len_j_str=get_divisors(len(j_str)))

        for k in get_divisors(len(j_str)):
            current_string = j_str[0:k]
            multiplikator = int(len(j_str)/k)
            new_word = current_string*multiplikator
            
            #debug(j_str=j_str, current_string=current_string, multiplikator=multiplikator, new_word=new_word)
            if j_str==new_word:
                solution+=j
                break

print(solution)
print(solution==correct_solution) 
        



        
