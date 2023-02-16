def checkprime(n):
    if n > 1:
        for i in range(2,int(n/2) +1):
            if (n % i) == 0:
                print("its not a prime number")
                break
        else:
            print("its a prime number")
    else:
        print("its not a prime number")
n = int(input())
checkprime(n)