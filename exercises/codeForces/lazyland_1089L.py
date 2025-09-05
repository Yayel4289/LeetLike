import math
n, k = map(int, input().split())
idlers = list(map(int, input().split()))
costs = list(map(int, input().split()))
todo = set((i for i in range(1, k+1)))
max_per_idler = {}
for i in range(n):
    todo.discard(idlers[i])
    if max_per_idler.get(idlers[i]) is None or \
       costs[i] > max_per_idler[idlers[i]][0]:
        max_per_idler[idlers[i]] = [costs[i], i]

if len(todo) == 0:
    print(0)
else:

    for pair in max_per_idler.values():
        costs[pair[1]] = math.inf

    costs.sort()
    cost = 0
    for i in range(len(todo)):
        cost += costs[i]
    print(cost)

