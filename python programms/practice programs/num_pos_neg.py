def numcheck(a):
    if a > 0:
        print("positive")
    elif a < 0:
        print("negative")
    else:
        print("its zero")
a = float(input())
numcheck(a)