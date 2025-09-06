n, m, c = map(int, input().split())
a = list(map(int, input().split())) # n times
b = list(map(int, input().split())) # m times

for i in range(n):
    if i + m <= n:
        for j in range(m):
            a[i + j] = (a[i + j] + b[j]) % c

for i in range(n):
    a[i] = str(a[i])
print(" ".join(a))

