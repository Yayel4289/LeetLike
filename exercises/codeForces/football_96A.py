MASK = 0b1111111

def check_danger(team, curr_mask, i):
    return (team & curr_mask) >> i == MASK

s = input()
n = len(s)
if n < 7:
    print("NO")
else:
    team = int(s, 2)
    inv_team = abs(~team ^ (2 ** n - 1)) - 1
    for i in range(n - 7 + 1):
        curr_mask = MASK << i
        if check_danger(team, curr_mask, i) or check_danger(inv_team, curr_mask, i):
            print("YES")
            break 
    else:
        print("NO")

