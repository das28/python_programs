n = int(input())
m = int(input())

for i in range(n,m+1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if i == sum:
            print(i)
