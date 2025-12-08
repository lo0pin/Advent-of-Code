from input import *

lines = data.splitlines()
myarray = []
newarray = []
final_result = 0

for line in lines:
    current_line = line.split(" ")
    myarray.append(current_line)


for i in myarray:
    for j in i:
        if j != '':
            newarray.append(j)

for  i in range(int(len(newarray)/5)):
    if (newarray[i+(int(len(newarray)/5))*4]) == "+":
        result =int(newarray[i+(int(len(newarray)/5))*0])+int(newarray[i+(int(len(newarray)/5))*1])+int(newarray[i+(int(len(newarray)/5))*2])+int(newarray[i+(int(len(newarray)/5))*3])
        final_result += result
        print("yolk")
    elif (newarray[i+(int(len(newarray)/5))*4]) == "*":
        print("molk")
        result =int(newarray[i+(int(len(newarray)/5))*0])*int(newarray[i+(int(len(newarray)/5))*1])*int(newarray[i+(int(len(newarray)/5))*2])*int(newarray[i+(int(len(newarray)/5))*3])
        final_result += result
        #print(newarray[i+(int(len(newarray)/5))*4])


print (final_result)
#print(newarray)
#print(len(newarray))

