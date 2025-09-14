n = int(input())
TEN_STEP_SUM = 45 # 1+2+...+9

def get_end_zeros(s):
    count = 0 
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            count += 1
        else:
            break 
    return count

def get_off_zeros_sum(s, end_zeros):
    total = 0
    for i in range(len(s) - end_zeros):
        total += int(s[i])
    return total

def i_step(i, s, b, end_zeros):
    off_zeros_sum = get_off_zeros_sum(s, end_zeros)

    if end_zeros == 0:
        return i + 1, off_zeros_sum

    step = 10**end_zeros
    new_i = i + step
    if new_i <= b:
        to_add = \
            off_zeros_sum * step + \
            end_zeros * 10**(end_zeros - 1) * TEN_STEP_SUM
        """
        1 0 ->                                          = 1*45
        2 0 -> 10 * 45 	+ 	10 * 45                     = 20 * 45 
        3 0 -> 100 * 45 +	100 * 45 	+ 	100 * 45	= 300 * 45 
        ...
        """
        return new_i, to_add
    else:
        return i_step(i, s, b, end_zeros - 1)


def digit_sum(a, b):
    i = a 
    total = 0
    while i <= b:
        s = str(i)
        end_zeros = get_end_zeros(s)
        i, to_add = i_step(i, s, b, end_zeros)
        total += to_add
    return total

for _ in range(n):
    a, b = map(int, input().split())
    print(digit_sum(a, b))

