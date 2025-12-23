"""
  ____             _          ______                    ____   _____ 
 |  _ \           | |        |  ____|                  |  _ \ / ____|
 | |_) |_ __ _   _| |_ ___   | |__ ___  _ __ ___ ___   | |_) | (___  
 |  _ <| '__| | | | __/ _ \  |  __/ _ \| '__/ __/ _ \  |  _ < \___ \ 
 | |_) | |  | |_| | ||  __/  | | | (_) | | | (_|  __/  | |_) |____) |
 |____/|_|   \__,_|\__\___|  |_|  \___/|_|  \___\___|  |____/|_____/ 
 """

from input import data
import time

tst = time.perf_counter()

coords = data.splitlines()

area = 0

correct_answer = 1525241870
#correct_answer = 1513988754

coord_points = []

def check_if_xyPoint_in_area(x, y):
    conditions_met = [0,0,0,0]
    coord_points.append(coord_points[0])
    for i in range(len(coord_points)-1):

        #alle bedingungen erfüllt: break
        if sum(conditions_met) == 4:
            break

        # x werte ident
        if coord_points[i][0] == coord_points[i+1][0]:

            #beide x-Bedingungen bereits erfüllt
            if conditions_met[0] and conditions_met[1]:
                continue

            #y-range definieren und überprüfen
            lower_y = min(coord_points[i][1],coord_points[i+1][1])
            upper_y = max(coord_points[i][1],coord_points[i+1][1])  
            if lower_y <= y <= upper_y:

                if coord_points[i][0] <= x and not conditions_met[0]:
                    conditions_met[0] = 1
                    
                if coord_points[i][0] >= x and not conditions_met[1]:
                    conditions_met[1] = 1


        
        #y werte ident
        elif coord_points[i][1] == coord_points[i+1][1]:
            #beide y-Bedingungen bereits erfüllt
            if conditions_met[2] and conditions_met[3]:
                continue

            #x-range definieren und überprüfen
            lower_x = min(coord_points[i][0],coord_points[i+1][0])
            upper_x = max(coord_points[i][0],coord_points[i+1][0])  
            if lower_x <= x <= upper_x:

                if coord_points[i][1] <= y and not conditions_met[2]:
                    conditions_met[2] = 1

                if coord_points[i][1] >= y and not conditions_met[3]:
                    conditions_met[3] = 1 

        else:
            print(f"Fehler: {coord_points[i]} und {coord_points[i+1]} passen nicht")

    del coord_points[-1]
    return sum(conditions_met) == 4

def check_if_all_four_corners_in_area(coord_a, coord_b):
    first_point = (coord_a[0], coord_b[1])
    secnd_point = (coord_b[0], coord_a[1])

    return check_if_xyPoint_in_area(first_point[0], first_point[1]) and check_if_xyPoint_in_area(secnd_point[0], secnd_point[1])

def return_all_four_points_of_rectangle(coord_a, coord_b):
    first_point = (coord_a[0], coord_b[1])
    secnd_point = (coord_b[0], coord_a[1])
    return (coord_a, first_point, coord_b, secnd_point)

def check_if_all_lines_of_rectangle_in_area(coord_a, coord_b):
    points = return_all_four_points_of_rectangle(coord_a, coord_b)
    range_steps = 10


    for i in range(min(points[0][1], points[1][1]),max(points[0][1], points[1][1]),range_steps):
        if not check_if_xyPoint_in_area(points[0][0], i):
            return False
        if not check_if_xyPoint_in_area(points[2][0], i):
            return False
        
    for i in range(min(points[1][0], points[2][0]), max(points[1][0], points[2][0]),range_steps):
        if not check_if_xyPoint_in_area(i, points[1][1]):
            return False
        if not check_if_xyPoint_in_area(i, points[3][1]):
            return False        
    return True

areas = []
for coord in coords:
    start = int(coord.split(",")[0])
    end = int(coord.split(",")[1])
    coord_points.append([start, end])


for first_coord in range(len(coord_points)):
    for second_cord in range(first_coord+1,len(coord_points)):
        if coord_points[first_coord][0] == coord_points[second_cord][0] or coord_points[first_coord][1] == coord_points[second_cord][1]:
            continue

        current_area = (abs(coord_points[second_cord][0]-coord_points[first_coord][0])+1) * (abs(coord_points[second_cord][1]-coord_points[first_coord][1])+1)
        
        areas.append((coord_points[first_coord], coord_points[second_cord], current_area))
        
        """if current_area > area:
            area = current_area"""

areas.sort(reverse=True, key=lambda a : a[2])

times=[]

#[49500:]
for i in areas[45000:]:
    progress = start/len(areas)*100
    print(f"\r{' ' * 40}", end="")         # alte Zeile wegwischen
    print(f"\r{progress:.6f} %", end="", flush=True)
    
    t0 = time.perf_counter()
    if check_if_all_four_corners_in_area(i[0], i[1]):
        if check_if_all_lines_of_rectangle_in_area(i[0], i[1]):
            print(f"\n{i[2]}")
            break
        t1 = time.perf_counter()
        if len(times)<2:
            times.append(t1-t0)
        else:
            current = t1-t0
            times[0]=min(current, times[0])
            times[1]=max(current, times[1])

 

tend = time.perf_counter()

print(f"gesamte Laufzeit: {tend - tst:.6f} s")
if times:
    print(f"min Laufzeit p itera: {times[0]:.6f} s")
if len(times)>1:
    print(f"max Laufzeit p itera: {times[1]:.6f} s")











