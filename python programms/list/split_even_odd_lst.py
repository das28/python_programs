lst = [1,4,8,2,45,88,4,5,1,33,45,7,84,]
even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)