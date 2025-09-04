import math
n, k = map(int, input().split())
mid = math.ceil(n / 2)
if k <= mid: # odds
    print(k * 2 - 1)
else:
    print((k - mid) * 2)

