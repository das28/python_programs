lst = [1,-3,4,6,8,5,7,-5,-4,-2,5,-4,9,-1]
neg = 0
even = 0
odd = 0

for i in lst:
    if i < 0 :
        neg += i
    elif i > 0 and i % 2 == 0:
        even += i
    elif i > 0 and i % 2 != 0:
        odd += i
print(neg)
print(even)
print(odd)