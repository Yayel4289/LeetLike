n = int(input())
sorted_a = sorted(map(int, input().split()), reverse=True)
mid = sum(sorted_a) / 2
total = 0
count = 0
for coin in sorted_a:
    count += coin 
    total += 1
    if count > mid:
        break
print(total)

