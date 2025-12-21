from input import data

coords = data.splitlines()

area = 0


coord_points = []

def in_area(x, y):
    conditions_met = 0
    coord_points.append(coord_points[0])
    for i in range(len(coord_points)):

        #x werte ident
        if coord_points[i][0] == coord_points[i+1][0]:
                
        
        #y werte ident
        else:



        """if coord_points[i][0] != coord_points[i+1][0]:
            continue
        if conditions_met > 0 and x<coord_points[i][0]:
            #print(coord_points[i][0], end=", ")
            continue
        lower_y = min(coord_points[i][1],coord_points[i+1][1])
        upper_y = max(coord_points[i][1],coord_points[i+1][1])
        if lower_y <= y <= upper_y:
            if conditions_met < 1:
                if coord_points[i][0] < x:
                    conditions_met += 1
                    print(conditions_met)

                    continue
            else:
                if coord_points[i][0] > x:
                    conditions_met += 1
                    break"""




    return conditions_met >= 2
    
areas = []
for coord in coords:
    start = int(coord.split(",")[0])
    end = int(coord.split(",")[1])
    coord_points.append([start, end])

#coord_points.sort(key=lambda pair: pair[0])
print(coord_points[:10])


for first_coord in range(len(coord_points)):
    for second_cord in range(first_coord+1,len(coord_points)):
        if coord_points[first_coord][0] == coord_points[second_cord][0] or coord_points[first_coord][1] == coord_points[second_cord][1]:
            #print("skippidi")
            continue

        current_area = abs(coord_points[second_cord][0]-coord_points[first_coord][0]+1) * abs(coord_points[second_cord][1]-coord_points[first_coord][1]+1)
        
        areas.append((coord_points[first_coord], coord_points[second_cord], current_area))
        
        """if current_area > area:
            area = current_area"""

areas.sort(reverse=True, key=lambda a : a[2])

print(areas[:5])
#print(area)

print(in_area(1733, 47000))


