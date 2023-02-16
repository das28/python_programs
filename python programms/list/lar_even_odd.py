def lar_even_odd(lst):
    even = []
    odd = []

    for i in lst:
        if i % 2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
        elif i == 0:
            print("0 is not even nor odd")
    return max(even) , max(odd)

lst=[0,5,8,4,9,2,6]
print(lar_even_odd(lst))
    

