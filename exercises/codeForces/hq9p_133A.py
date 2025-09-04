p = input()
instructions = ("H", "Q", "9")
for i, letter in enumerate(p):
    if letter in instructions:
            print("YES")
            break
else:
    print("NO")

