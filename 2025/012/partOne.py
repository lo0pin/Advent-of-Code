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
print(forms[:5])"""   

############## FUNKTIONEN ##############



