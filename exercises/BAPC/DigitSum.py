import math
def decompose(i):
    res = 0
    while i >= 10:
        if i%10==0:
            i = i//10
            inter = i/10
        else:
            inter = (i/10)
        res = res + (10 * (inter - rounding(i/10)))
        i = rounding(i/10)
    return res+i

def rounding(i):
    res = math.trunc(i)
    if res - i > 0:
        res = math.trunc(i-0.5)
    return res

def digitSum(i,j):
    res = 0
    first = i
    addi = (decompose(i)) 
    while i<= j:
        if i%10==0 and i!=first:
            addi= decompose(i)
        i = i+1
        res=res+addi
        addi+=1
    return round(res)

print(digitSum(0,10))
print(digitSum(28,31))
print(digitSum(1234,56789))
print(digitSum(10,20))
print(digitSum(20,30))
print(digitSum(1,2))
print(digitSum(12,83))

