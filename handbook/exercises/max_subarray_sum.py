from random import randint
def max_subarray_sum(arr):
    curr = 0
    best = 0
    for x in arr:
        if -x >= curr:
            curr = 0
            continue
        curr += x
        if curr > best:
            best = curr
    return best

def solution(arr): # same idea better
    best = curr = 0
    for x in arr:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best

l = [randint(-10, 10) for _ in range(randint(5, 10))]
print(l, max_subarray_sum(l), sep="\n")
print(l, solution(l), sep="\n")
