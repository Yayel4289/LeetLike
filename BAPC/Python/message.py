entry = input().split()
n, m = int(entry[0]), int(entry[1])
grid = ""
for i in range(n):
    grid += input().replace(".", "")
print(grid)


