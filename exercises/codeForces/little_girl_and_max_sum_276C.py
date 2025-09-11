# helped : use differences and prefix sum

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
freq = [0] * (n + 1) # diff_arr
for _ in range(q):
    l, r = map(int, input().split())
    freq[l - 1] += 1 # start
    freq[r] -= 1 # stop

# prefix sum
for i in range(1, n + 1):
    freq[i] += freq[i - 1]

freq.sort(reverse=True)

total = 0
for i in range(n):
    if a[i] == 0 or freq[i] == 0:
        break
    total += a[i] * freq[i]
print(total)

