from input import data, data2


########## DATENAUFBEREITUNG ###########

forms = (data.split("\n"))
forms = [i for i in forms if i.startswith("#") or i.startswith(".")]
forms = [(forms[i],forms[i+1], forms[i+2]) for i in range(0,len(forms),3)]

instructions = data2.splitlines()
for i in range(len(instructions)):
    instructions[i] = instructions[i].replace("x", " ").replace(":", "")
    field = instructions[i].split(" ")[:2]
    for j in range(len(field)):
        field[j] = int(field[j])
    number = instructions[i].split(" ")[2:]
    for k in range(len(number)):
        number[k] = int(number[k])
    field = tuple(field)
    number = tuple(number)
    instructions[i] = (field, number)

"""print(instructions[:10])
print(forms[:5]) """  

############## FUNKTIONEN ##############

#returnt eine Form (input) um 90° nach rechts gedreht
def turn_right(tupl_inp):
    result = []
    for i in range(3):
        for j in range(2,-1,-1):
            result.append((tupl_inp[j][i]))
    returny = []
    for i in range(0,9,3):
        returny.append((result[i] + result[i+1] + result[i+2]))
    return tuple(returny)

#returnt eine Form(input) über die horizontale Achse gespiegelt
def mirror_over_y_axe(tupl_inp):
    result=[]
    for i in range(3):
        result.append(tupl_inp[i][2]+tupl_inp[i][1]+tupl_inp[i][0])
    return tuple(result)

#returnt alle möglichen variationen einer Form (input) nach allen möglichen Drehungen und Spiegelungen
def alle_welten_einer_form(tupl_inp):
    result = [tupl_inp]
    result.append(mirror_over_y_axe(tupl_inp))
    for i in range(3):
        result.append(turn_right(result[-2]))
        result.append(turn_right(result[-2]))
    return result
    
def print_form(tupl_inp):
    for i in tupl_inp:
        print(i[0] +" "+ i[1] +" "+ i[2])
    print()


################# CODE #################

for i in alle_welten_einer_form(forms[0]):
    print_form(i)

print(alle_welten_einer_form(forms[0]))

"""print_form(forms[0])
print_form(turn_right(forms[0]))
print_form(mirror_over_y_axe(turn_right(forms[0])))"""




