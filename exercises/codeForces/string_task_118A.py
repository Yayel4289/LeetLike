VOWELS = "aeiouy"
s = list(input().lower())
s = filter(lambda x: x not in VOWELS, s)
tmp = ".".join(s)
print(("." if len(tmp) > 0 else "") + tmp)

