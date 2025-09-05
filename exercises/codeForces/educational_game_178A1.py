import math

def find_min_moves(n, a, k):
    if k == -1:
        return 0
    # i = 0
    t = math.ceil(math.log2(n)) - 1
    # a[0] -= a[0]
    a[2**t] += a[0]
    return a[0] + find_min_moves(n - 1, a[1:], k - 1)
    

n = int(input())
a = list(map(int, input().split()))
for k in range(n - 1):
    print(find_min_moves(n, a.copy(), k))

