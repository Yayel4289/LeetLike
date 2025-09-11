# helped but obvious, time for a break
def solve():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] in ("0", "8"):
            return int(s[i])
    for i in range(n):
        if s[i] == "0":
            continue
        for j in range(i+1, n):
            x = int(s[i] + s[j])
            if not x % 8:
                return x

    for i in range(n):
        if s[i] == "0":
            continue
        for j in range(i+1, n):
            for k in range(j+1, n):
                x = int(s[i] + s[j] + s[k])
                if not x % 8:
                    return x
    
    return -1

res = solve()
if res == -1:
    print("NO")
else:
    print("YES")
    print(res)
