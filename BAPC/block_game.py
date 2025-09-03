# helped
n, m = map(int, input().split())

if n > m:
    n, m = m, n

turn = 0 # player turn
while True:
    if m % n == 0 or m // n >= 2:
        print("win" if turn == 0 else "lose")
        break
    n, m = m - n, n
    if n > m:
        n, m = m, n
    turn ^= 1

