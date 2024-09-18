def dist_point(p0, p1):
    x_a, y_a = p0
    x_b, y_b = p1
    return ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5


def dist_seg(seg0, seg1):
    pass

def input_to_point():
    point = input().split()
    return int(point[0]), int(point[1])


def get_polygon(n):
    polygon = []
    for i in range(n):
        polygon.append(input_to_point())
    return tuple(polygon)


num_test_case = int(input())
for i in range(num_test_case):
    ni = int(input())
    inner_polygon = get_polygon(ni)
    no = int(input())
    outer_polygon = get_polygon(no)

