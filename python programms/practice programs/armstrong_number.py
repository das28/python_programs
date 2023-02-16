n = int(input())
res = 0
temp = n
l = len(str(n))

while n > 0:
    rem = n % 10
    res = res + rem ** l
    n = n // 10

if res == temp:
    print("This is armstroge number")
else:
    print("This is not an armstrong number")
