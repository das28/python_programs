def checkleap(n):
    if ((n % 400) == 0 or
       (n % 100 != 0) and
       (n % 4 == 0)):
       print("this is a leap year")
    else:
        print("this is NOT a leap year")
n = int(input())
checkleap(n)