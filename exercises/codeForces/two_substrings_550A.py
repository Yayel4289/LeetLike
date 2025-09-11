s = input()

def sol(s):
    n = len(s)
    if n < 4:
        return False
    AB = BA = False 
    i = 0
    while i < n - 1:
        curr = s[i: i+2]
        if not AB and curr == "AB":
            AB = True 
            i += 2
        elif not BA and curr == "BA":
            BA = True
            i += 2 
        else:
            i += 1

        if AB and BA:
            return True

    return False

print("YES" if sol(s) or sol(s[::-1]) else "NO")

