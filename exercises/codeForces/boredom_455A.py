
def get_min_max(l):
    return (0, 1) if l[0] < l[1] else (1, 0)

n = int(input())
l = []
for a_k in map(int, input().split()):
    while a_k >= len(l):
        l.append(0)
    l[a_k] += a_k
l.append(0)

tmp = [0, 0]
score = 0
for i in l[1:]:
    min_i, max_i = get_min_max(tmp)
    if tmp[min_i] + i > tmp[max_i]:
        tmp[min_i] += i
    else:
        score += tmp[max_i]
        tmp = [0, 0]
print(score)

