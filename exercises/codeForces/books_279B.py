n, t = map(int, input().split())
a = list(map(int, input().split()))

max_books = -1 
books = 0
count = 0
i = j = 0
while i < n:
    while j < n and count + a[j] <= t:
        count += a[j]
        books += 1
        j += 1
    if books > max_books:
        max_books = books
    count -= a[i]
    books -= 1
    i += 1 

print(max_books)

