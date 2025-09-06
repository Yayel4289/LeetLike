import math

n, l = map(int, input().split())
a = sorted(list(set(map(int, input().split()))))

a = [0] + a + [l]
new_n = len(a) - 1
max_d = -math.inf
for i in range(new_n):
    div = 2 if 0 < i < new_n - 1 else 1
    d = (a[i + 1] - a[i]) / div
    if d > max_d:
        max_d = d
print(max_d)

