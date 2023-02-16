n = int(input())
n1 = 0
n2= 1
count = 0

for i in range(0,n+1):
    print(n1)
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1
