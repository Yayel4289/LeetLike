def bin_false_insert(arr, x):
    n = len(arr)
    b = n // 2
    k = 0
    while b >= 1:
        while b + k < n and arr[b + k] <= x:
            k += b
        b //= 2
    return k if x < arr[0] else k + 1

n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

for _ in range(q):
    m_i = int(input())
    print(bin_false_insert(x, m_i))

