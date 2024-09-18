def dist(a, b):
    x_a, y_a = a
    x_b, y_b = b
    return ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5


def middle(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return (x0 + x1) / 2, (y0 + y1) / 2


def mediator(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return x1 - x0, y1 - y0, ((x1 - x0) ** 2 + (y1 - y0) ** 2) / 2


def inter(d0, d1):
    a0, b0, c0 = d0
    a1, b1, c1 = d1
    det = a0 * b1 - a1 * b0

    x = (c0 * b1 - c1 * b0) / det
    y = (a0 * c1 - a1 * c0) / det
    return x, y


def input_to_point():
    point = input().split()
    return int(point[0]), int(point[1])


def get_even_radius(n, inner):
    p0 = input_to_point()
    first_point = ()
    p1 = ()
    for i in range(n - 1):
        if i == (n - 1) // 2:
            p1 = input_to_point()
        elif (not inner) and i == 0:
            first_point = middle(input_to_point(), p0)
        else:
            input()
    if inner:
        first_point = p0
    center = middle(p0, p1)
    return dist(first_point, center)


def get_odd_radius(n, inner):
    p0 = input_to_point()
    p1 = input_to_point()
    p2 = input_to_point()
    print(p0, p1, p2)
    if inner:
        first_point = p0
    else:
        first_point = middle(p0, p1)
    for i in range(n - 3):
        input()
    d0 = mediator(p0, p1)
    d1 = mediator(p1, p2)
    center = inter(d0, d1)
    return dist(first_point, center)


def get_radius(n, inner):
    if n % 2:
        return get_odd_radius(n, inner)
    else:
        return get_even_radius(n, inner)


num_test_case = int(input())
for i in range(num_test_case):
    ni = int(input())
    inner_radius = get_radius(ni, True)
    no = int(input())
    outer_radius = get_radius(no, False)
    max_radius = (outer_radius - inner_radius) / 2
    print(outer_radius, "-", inner_radius)
    print(max_radius)
    print("-" * 50)
