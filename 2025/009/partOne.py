from input import *

coords = data.splitlines()

area = 0

coord_points = []
for coord in coords:
    start = int(coord.split(",")[0])
    end = int(coord.split(",")[1])
    coord_points.append([start, end])

coord_points.sort(key=lambda pair: pair[0])

for first_coord in range(len(coord_points)):
    for second_cord in range(first_coord+1,len(coord_points)):
        if coord_points[first_coord][0] == coord_points[second_cord][0] or coord_points[first_coord][1] == coord_points[second_cord][1]:
            #print("skippidi")
            continue
        current_area = abs(coord_points[second_cord][0]-coord_points[first_coord][0]+1) * abs(coord_points[second_cord][1]-coord_points[first_coord][1]+1)
        if current_area > area:
            area = current_area

print(area)

