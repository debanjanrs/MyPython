nums = [5, 10, 5, 6, 3]
count = 0
count_p = 0

for j in nums:
    if j == 5:
        count = count + 1
    if j == 6:
        count_p = count_p + 1

print(count)
print(count_p)
