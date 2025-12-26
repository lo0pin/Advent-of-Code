from input import data, data2
from copy import deepcopy


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

"""print(instructions[:10])"""
"""print(forms[:5]) """  

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
    for i in range(len(result)-1,-1,-1):
        if result.count(result[i]) > 1:
            del result[i]
    return result
    
def print_form(tupl_inp):
    for i in tupl_inp:
        print(i[0] +" "+ i[1] +" "+ i[2])
    print()

def calculate_platz(inpu):
    width = inpu[0][0]
    lenght = inpu[0][1]
    lines = [["."] for n in range(width)]
    area = [deepcopy(lines) for n in range(lenght)]
    return area

"""print(calculate_platz(instructions[0])[0])"""

#def calulate_bedarfe()
"""sums = []
areas = []"""
#quick ckeck, if total area > sum of forms * 9
#and can be skipped, cos of vast space
def easy_check(instru):
    area = instru[0][0]*instru[0][1]
    #areas.append(area)
    summy = 0
    
    for i in enumerate(instru[1]):
        summy += i[1] * "".join(forms[i[0]]).count("#")
        #sums.append(summy)
    if summy>area:
        return False
    
    
    return area > sum(instru[1])*9

def check_a_little_less_easy(instru):
    mein_blokko = list(instru[1])
    breite = instru[0][0]
    hoehe = instru[0][1]
    area = breite*hoehe

    subtrahend_one = min(mein_blokko[2], mein_blokko[4], mein_blokko[5])
    subtrahend_two = min(mein_blokko[3], mein_blokko[0])

    area_ugu_bloecke = subtrahend_one * 3 * 6
    area_magi_bloeke = mein_blokko[1] * 4 *4 / 2
    area_sheg_bloeke = subtrahend_two * 5 * 8 / 2

    ergebniiiiis = area_ugu_bloecke + area_magi_bloeke + area_sheg_bloeke
    condition_one = area > ergebniiiiis
    
    
    """list_for_bedingung_two = [(1, area-ergebniiiiis), [mein_blokko[0]-subtrahend_two, 0, mein_blokko[2]-subtrahend_one, mein_blokko[3]-subtrahend_two, mein_blokko[4], mein_blokko[5]]]
    condition_two = easy_check(list_for_bedingung_two)
"""
    return condition_one #and condition_two




################# CODE #################

print(instructions[0])

easychecktrue = 0
easychecknope = 0

for i in instructions:
    if easy_check(i):
        easychecktrue += 1
    if check_a_little_less_easy(i):
        easychecknope += 1

print (str(easychecktrue) + "\t" + str(easychecknope) + "\t" + str(len(instructions)))




"""for i in alle_welten_einer_form(forms[3]):
    print_form(i)"""


"""
print(alle_welten_einer_form(forms[1]))
"""

"""for i in forms:
    for j in i:
        print(j)
    print()"""

"""print_form(forms[0])
print_form(turn_right(forms[0]))
print_form(mirror_over_y_axe(turn_right(forms[0])))"""



