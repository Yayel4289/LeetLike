n = int(input())
s = list(map(int, input().split()))

nums = [0 for _ in range(5)]
for si in s:
    nums[si] += 1

taxi_4 = nums[4]
nums[4] = 0
count = taxi_4

taxi_31 = min(nums[1], nums[3])
nums[1] -= taxi_31
nums[3] -= taxi_31
count += taxi_31

taxi_22 = nums[2] // 2
nums[2] -= 2*taxi_22
count += taxi_22

taxi_211 = min(nums[1] // 2, nums[2])
nums[1] -= 2*taxi_211
nums[2] -= taxi_211
count += taxi_211

taxi_1111 = nums[1] // 4 
nums[1] -= 4*taxi_1111
count += taxi_1111

if nums[1] or nums[2]:
    count += 1

count += nums[3]

print(count)
