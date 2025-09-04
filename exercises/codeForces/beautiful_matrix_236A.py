def manhattan_dist(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2 
    return abs(x2 - x1) + abs(y2 - y1)

coor = tuple()
for i in range(1, 6):
    s = input().split()
    for j in range(1, 6):
        if s[j-1] == "1":
            coor = (i, j)
            break

print(manhattan_dist(coor, (3, 3)))

