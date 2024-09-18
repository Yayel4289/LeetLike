entry = input()
list_entry = entry.split(";")
res = 0
for data in list_entry:
    if "-" in data:
        nums = data.split("-")
        res += int(nums[1]) - int(nums[0]) + 1
    else:
        res += 1
print(res)

