from math import ceil

def grow_side(side, a):
    return a * ceil(side / a)

n, m, a = map(int, input().split())
new_n = grow_side(n, a)
new_m = grow_side(m, a)
area = new_n * new_m
flagstone_surface = a*a
print(area // flagstone_surface)

