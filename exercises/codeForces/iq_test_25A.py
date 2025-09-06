n = int(input())
l = list(map(int, input().split()))

odds = []
evens = []
for i in range(3):
    if l[i] & 1:
        odds.append(i)
    else:
        evens.append(i)

if len(odds) == 1:
    print(odds[0] + 1)
elif len(evens) == 1:
    print(evens[0] + 1)
else:
    search_odds = True if len(odds) == 0 else False
    for i in range(3, n):
        if l[i] & 1 == search_odds:
            print(i + 1)

