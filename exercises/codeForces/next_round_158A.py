n, k = map(int, input().split())
count = 0
limit = 1
for i, x in enumerate(map(int, input().split())):
    if i+1 == k:
        limit = max(limit, x)
    if x >= limit:
        count += 1
print(count)
    
