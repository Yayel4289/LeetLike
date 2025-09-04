def renew_output(output, op):
    if op in (output, '='):
        return output
    if output == '=':
        return op
    return '?'

def get_output(s):
    output = s[0]
    for op in s[1:]:
        output = renew_output(output, op)
    return output


t = int(input())
for _ in range(t):
    print(get_output(input()))
