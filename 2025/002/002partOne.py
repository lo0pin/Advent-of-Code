input_num = "26803-38596,161-351,37-56,9945663-10044587,350019-413817,5252508299-5252534634,38145069-38162596,1747127-1881019,609816-640411,207466-230638,18904-25781,131637-190261,438347308-438525264,5124157617-5124298820,68670991-68710448,8282798062-8282867198,2942-5251,659813-676399,57-99,5857600742-5857691960,9898925025-9899040061,745821-835116,2056-2782,686588904-686792094,5487438-5622255,325224-347154,352-630,244657-315699,459409-500499,639-918,78943-106934,3260856-3442902,3-20,887467-1022885,975-1863,5897-13354,43667065-43786338"

ranges = input_num.split(",")
solution = 0

for i in ranges:
    current_list = i.split("-")
    #print(i)
    start = int(current_list[0])
    end = int(current_list[1])
#     print(start)
#     print(end)
#     print("_____")
#    if i[0] == "1":
#    print(i)
    if len(str(start))%2==1 and len(str(end))%2==1: #sequences mit ausschließlich zahlen mit ungeraden längen filtern
            continue
    for j in range(start, end+1): #alle Zahlen iterieren
        if len(str(j)) %2==1: #ungerade Längen überspringen
            continue
        current_word = str(j)
        current_len = int(len(current_word)/2)
        if current_word[0:current_len] == current_word[current_len:]:
             solution += j
        
#         if str(j)[0] == "0":
#        print(j)
print (solution)

        
