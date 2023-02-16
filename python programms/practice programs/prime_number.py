n = int(input())
m = int(input())

for i in range(n,m):
    for j in range(2,n):
        if i % j == 0 :
            break 
    else:
        print(i, end=" ")