lst = [1,2,4,6,8,5,3,2,5,7,9,24,5,6,7,3,4,5,6,7]
target = 5
count = 0
for i in lst:
    if i == target:
        count += 1
print(target,count)