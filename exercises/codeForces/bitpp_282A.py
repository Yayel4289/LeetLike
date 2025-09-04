n = int(input())
x = 0
for i in range(n):
    s = input()
    if '+' in s:
        x += 1
    elif '-' in s:
        x -= 1
print(x)
